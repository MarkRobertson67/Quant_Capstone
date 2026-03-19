from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("KRAKEN_API_KEY")
API_SECRET = os.getenv("KRAKEN_API_SECRET")

print("Key loaded:", API_KEY[:6], "...")
