import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
class Config:

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GOOGLE_MODEL = os.getenv("GOOGLE_MODEL")

    SOLITAIR_URL = os.getenv("SOLITAIR_URL")
    ORIGIN_LINK = os.getenv("ORIGIN_LINK")

    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

    EMAIL01 = os.getenv("EMAIL01")
    EMAIL02 = os.getenv("EMAIL02")

   