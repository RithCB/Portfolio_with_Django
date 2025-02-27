import os 
from dotenv import load_dotenv

load_dotenv()
print("Name",os.getenv("DB_NAME"))
print("User",os.getenv("DB_USER"))
print("Password",os.getenv("DB_PASSWORD"))
print("Host", os.getenv("DB_HOST"))
print("Port",os.getenv("DB_PORT"))