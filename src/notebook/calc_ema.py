import numpy as np

# EMA = (current*K) + (EMA * (1-K))
def calculate_ema(prices, period):
    ema = [np.mean(prices[:period])]
    multiplier  = 2/(period + 1) #k

    for price in prices[period:]:
        new_ema = (price * multiplier) + (ema[-1] * (1-multiplier))
        ema.append(new_ema)

    return np.array(ema)



prices = [10, 20, 30, 40]
ema = calculate_ema(prices, period=3)
print("EMA:", ema)
