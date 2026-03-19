from dotenv import load_dotenv
import os

load_dotenv()

def test_api_keys():
    key = os.getenv("KRAKEN_API_KEY")
    secret = os.getenv("KRAKEN_API_SECRET")

    assert key is not None
    assert secret is not None
    