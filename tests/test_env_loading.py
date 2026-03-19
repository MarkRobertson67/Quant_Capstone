from dotenv import load_dotenv
import os

def test_env_variables():
    load_dotenv()
    assert os.getenv("KRAKEN_API_KEY") is not None
    assert os.getenv("KRAKEN_API_SECRET") is not None
    