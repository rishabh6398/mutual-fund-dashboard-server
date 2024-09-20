from dotenv import load_dotenv
import os

load_dotenv()

DUMMY_USERNAME = os.getenv('DUMMY_USERNAME')
DUMMY_PASSWORD = os.getenv('DUMMY_PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
RAPIDAPI_HOST = os.getenv('RAPIDAPI_HOST')
RAPIDAPI_URL = os.getenv('RAPIDAPI_URL')

# Add CORS origins
origins = [
    "http://localhost:3000",
    "http://localhost:8000"
]
