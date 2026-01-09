from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = str =  os.getenv("SECRET_KEY")
ALGORITHM = str = os.getenv("ALGORITHM")
ACCESS_TOKEN_MUNUTE = int(os.getenv("ACCESS_TOKEN_MUNUTE" , 30))