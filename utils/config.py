import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("BASE_URL")
USERNAME = os.getenv("ADMIN_USERNAME")
PASSWORD = os.getenv("ADMIN_PASSWORD")