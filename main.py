import yaml
import os


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def main():
    print("🚀 Quant Capstone Bot starting...")

    # Load configs
    live_config = load_yaml("configs/live_config.yaml")
    strategy_config = load_yaml("configs/strategy_config.yaml")

    # Determine mode (ENV overrides YAML)
    mode = os.getenv("MODE", live_config["live_trading"]["mode"])

    print(f"⚙️ Mode: {mode}")

    if mode == "paper":
        print("📝 Running paper trading...")
        # TODO: hook in paper trading engine
        # from execution.paper_trader import run_paper
        # run_paper()

    elif mode == "live":
        print("💰 Running LIVE trading...")
        # TODO: hook in live trading engine
        # from execution.live_trader import run_live
        # run_live()

    elif mode == "backtest":
        print("📊 Running backtest...")
        # TODO: hook in backtest engine
        # from research.backtest import run_backtest
        # run_backtest()

    else:
        raise ValueError(f"❌ Invalid mode: {mode}")

    print("✅ Execution finished.")


if __name__ == "__main__":
    main()