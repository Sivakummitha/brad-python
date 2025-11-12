from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
debug_mode = os.getenv("DEBUG")
print("API Key:", api_key)
print("Database User:", db_user)
print("Debug Mode:", debug_mode)
