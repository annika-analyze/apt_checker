import requests
from units import Unit
import json
import datetime
import logging

logger = logging.Logger(__name__)

def get_available_units(url, origin, favorite_layouts):

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Origin": origin,
        "Referer": origin,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",  # Looks like a real browser
    }

    response = requests.get(url, headers=headers)

    if response.ok:

        data = response.json()
        units = data.get("units_data").get("units")
        
        if units:
            logger.info(f"DATA RETRIEVED: {datetime.datetime.now()}")
            unit_list = [Unit(u) for u in units if u.get("layoutId") in favorite_layouts]
            return unit_list
        
        logger.error("No Data Retrieved :( ")            
           
    else:
        logger.error(f"Request failed with status {response.status_code}")



def fromat_unit_alert_prompt(units, link):
    unit_str = [str(unit) for unit in units if unit.layoutName == "B"]

    prompt = f"""" 
        Please format the following list of apartments into a friendly email alert. 
        Make sure to make the email exciting and fun to read, so use emojis and exclamation points for the intro and outro.
        You can even say girlll, slayyy, gucci gang, or any other fun words if you want to! 
        Create something original, bold, and unexpected.

        For the body of the email, please include the following information for each apartment:
            - Price
            - Available date (Please format this as "Available on: MM/DD/YYYY")

        Put apartment 2004 first, and then the rest in order of price low to high.
        This information should be formatted neatly for easy reading. Do not use astericks, just bullet points or dashes,
        and a space between each apartment.

        Include the following information at the end of the email:
        - This link: {link}.
        - And tell my girlfriend to text me if she has any questions!
        - The date and time of the email
        - From: Apartment Bot Bestie 💌

        Only respond with the information, as if you were typing the body of an email! We don't need a subject line.
        Here is the list of apartments:
        {unit_str}

    """

    return prompt

