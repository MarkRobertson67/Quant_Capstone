import sys
import os
import yaml
import pandas as pd
from dotenv import load_dotenv

def main():
    print("🚀 Quant Capstone Bot starting...")
    print(f"Python version: {sys.version}")

    # Load environment variables
    load_dotenv()
    api_key = os.getenv("KRAKEN_API_KEY")
    api_secret = os.getenv("KRAKEN_API_SECRET")

    if not api_key or not api_secret:
        print("⚠️ Missing API keys in .env file!")
    else:
        print("✅ API keys loaded (hidden for safety):", api_key[:4] + "****")

    # Load config
    try:
        with open("configs/live_config.yaml", "r") as f:
            config = yaml.safe_load(f)

        # Inject API keys from environment into config
        config["exchange"]["api_key"] = api_key
        config["exchange"]["api_secret"] = api_secret

        print("✅ Loaded config:")
        print(config)

    except FileNotFoundError:
        print("⚠️ No config found at configs/live_config.yaml")
    except Exception as e:
        print("⚠️ Failed to load config:", e)

    # Simple data test
    try:
        df = pd.DataFrame({"price": [100, 101, 102], "volume": [5, 7, 6]})
        print("✅ Dummy dataframe created:")
        print(df)
    except Exception as e:
        print("⚠️ Pandas test failed:", e)

    print("🎉 Main script finished successfully.")

if __name__ == "__main__":
    main()
