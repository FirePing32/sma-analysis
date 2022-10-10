import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def sma(data, sma1, sma2):
    df = pd.DataFrame.from_dict(data)

    df = df.set_index('date')
    df[f'{sma1}_SMA'] = df['close'].rolling(window=sma1, min_periods=1).mean()
    df[f'{sma2}_SMA'] = df['close'].rolling(window=sma2, min_periods=1).mean()
    df['Signal'] = 0.0
    df['Signal'] = np.where(df[f'{sma1}_SMA'] > df[f'{sma2}_SMA'], 1.0, 0.0)
    df['Position'] = df['Signal'].diff()

    plt.figure(figsize=(20, 10))
    # plot close price, short-term and long-term moving averages
    df['close'].plot(color='k', label='close')
    df[f'{sma1}_SMA'].plot(color='b', label=f'{sma1}-day SMA')
    df[f'{sma2}_SMA'].plot(color='g', label=f'{sma2}-day SMA')
    plt.plot(df[df['Position'] == 1].index,
            df[f'{sma1}_SMA'][df['Position'] == 1],
            '^', markersize=15, color='g', label='buy')
    plt.plot(df[df['Position'] == -1].index,
            df[f'{sma1}_SMA'][df['Position'] == -1],
            'v', markersize=15, color='r', label='sell')
    plt.ylabel('Price in Rupees', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title('HINDALCO', fontsize=20)
    plt.legend()
    plt.grid()
    plt.show()
