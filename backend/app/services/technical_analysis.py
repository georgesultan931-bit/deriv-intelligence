from statistics import mean, pstdev


def sma(values: list[float], period: int) -> float:
    window = values[-period:]
    return round(mean(window), 4)


def ema(values: list[float], period: int) -> float:
    multiplier = 2 / (period + 1)
    value = values[0]
    for price in values[1:]:
        value = price * multiplier + value * (1 - multiplier)
    return round(value, 4)


def rsi(values: list[float], period: int = 14) -> float:
    gains = []
    losses = []
    for previous, current in zip(values[-period - 1 : -1], values[-period:]):
        delta = current - previous
        gains.append(max(delta, 0))
        losses.append(abs(min(delta, 0)))
    average_gain = mean(gains) if gains else 0
    average_loss = mean(losses) if losses else 0
    if average_loss == 0:
        return 100.0
    rs = average_gain / average_loss
    return round(100 - (100 / (1 + rs)), 2)


def macd(values: list[float]) -> dict[str, float]:
    macd_line = ema(values, 12) - ema(values, 26)
    signal = ema(values[-18:] + [macd_line], 9)
    return {"macd": round(macd_line, 4), "signal": round(signal, 4), "histogram": round(macd_line - signal, 4)}


def bollinger_bands(values: list[float], period: int = 20) -> dict[str, float]:
    window = values[-period:]
    center = mean(window)
    deviation = pstdev(window)
    return {"upper": round(center + 2 * deviation, 4), "middle": round(center, 4), "lower": round(center - 2 * deviation, 4)}


def support_resistance(values: list[float]) -> dict[str, float]:
    recent = values[-36:]
    return {"support": round(min(recent), 4), "resistance": round(max(recent), 4)}


def analyze(values: list[float]) -> dict[str, object]:
    ema_fast = ema(values, 12)
    ema_slow = ema(values, 26)
    current_rsi = rsi(values)
    trend = "Bullish" if ema_fast > ema_slow else "Bearish"
    volatility = pstdev(values[-20:])
    return {
        "sma_20": sma(values, 20),
        "ema_12": ema_fast,
        "ema_26": ema_slow,
        "rsi_14": current_rsi,
        "macd": macd(values),
        "bollinger": bollinger_bands(values),
        "levels": support_resistance(values),
        "trend": trend,
        "volatility": round(volatility, 4)
    }


