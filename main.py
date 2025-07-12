# main.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Download data
    data = yf.download('SPY', start='2020-01-01', end='2024-12-31', auto_adjust=True)

    # Calculate 20-day SMA
    data['SMA20'] = data['Close'].rolling(window=20).mean()

    # Drop rows with NaN
    plot_data = data[['Close', 'SMA20']].dropna()

    # Plot
    plt.figure(figsize=(14, 6))
    sns.lineplot(x=plot_data.index, y=plot_data['Close'].squeeze(), label='Close')
    sns.lineplot(x=plot_data.index, y=plot_data['SMA20'].squeeze(), label='20-day SMA')
    plt.title('SPY Close Price & 20-day SMA')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()          # ← Prevents clipping
    plt.savefig("output/spy_plot.png")  # ← Saves image to file
    # plt.show()  # Optional if running in GUI


if __name__ == "__main__":
    main()
