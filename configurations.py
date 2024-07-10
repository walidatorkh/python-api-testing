from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv('BASE_URL')
users_api_url = os.getenv('USER_API_URL')

print(os.getenv('BASE_URL'))
print(os.getenv('USER_API_URL'))
