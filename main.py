from get_apts import get_available_units, fromat_unit_alert_prompt
from messager import send_email
from llm import generate_response
from config import Config
import time
import logging

if __name__ == "__main__":

    start_time = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting the script...")
    logging.info(f"Script started at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

    favorite_layouts = [
        "23c89409-b91f-425b-aee0-08aed27440a4" , 
        "b213b78d-ab32-4203-b2fd-9ec95ab513e3",
        "14622c56-b93c-4a57-9def-b10da5e960c2" 
    ]

    try:
        logging.info(f"Fetching available units started")
        current_units = get_available_units(
            url = Config.SOLITAIR_URL, 
            origin = Config.ORIGIN_LINK,
            favorite_layouts = favorite_layouts
        )
        logging.info(f"Available units fetched successfully")
    except Exception as e:
        logging.error(f"Error when fetching available units: {str(e)}")
        current_units = []
        logging.info(f"Using empty list for current units")
        current_units = []

    
    prompt = fromat_unit_alert_prompt(current_units, Config.ORIGIN_LINK)
    logging.info(f"Prompt generated")

    try:
        logging.info(f"Google API Request started")
        body = generate_response(
            prompt=prompt,
            model=Config.GOOGLE_MODEL,
            api_key=Config.GOOGLE_API_KEY
        )
        logging.info(f"Google API response generated")

        if not body:
            raise ValueError("No response from Google API")
        
    except Exception as e:
        logging.error(f"Error when calling Google API: {str(e)}")
        body = "Error generating email content. Please check the logs. :("


    end_time = time.time() 
    elapsed_time = end_time - start_time
    logging.info(f"Script finished at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    body += "Script took " + str(round(elapsed_time, 2)) + " seconds to run.\n\n"

    try:
        logging.info(f"Sending emails started")
        send_email(
            sender_email= Config.SENDER_EMAIL,
            # receiver_emails=[Config.EMAIL01],
            receiver_emails=[Config.EMAIL01, Config.EMAIL02],
            subject="🔔🏠 Apartment Bot Update!",
            body = body,
            password=Config.SENDER_PASSWORD
        )
        logging.info(f"Successfully sent emails!")
    except Exception as e:
        logging.error(f"Error when sending emails: {str(e)}")

    

    
    
   







    

   