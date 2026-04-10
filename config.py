import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")


EMAIL_USER = os.getenv("[EMAIL_ADDRESS]")
EMAIL_PASS = os.getenv("[EMAIL_PASSWORD]")