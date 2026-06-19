import math
import random
from datetime import datetime, timezone

from app.schemas import AssetQuote

ASSETS = {
    "R_100": "Volatility 100 Index",
    "R_75": "Volatility 75 Index",
    "BOOM1000": "Boom 1000 Index",
    "CRASH500": "Crash 500 Index"
}


def current_quotes() -> list[AssetQuote]:
    quotes: list[AssetQuote] = []
    for index, (symbol, name) in enumerate(ASSETS.items()):
        base = 900 + index * 2400
        wave = math.sin(datetime.now(timezone.utc).timestamp() / 60 + index) * 14
        noise = random.uniform(-6, 6)
        change = round((wave + noise) / 10, 2)
        price = round(base + wave + noise, 2)
        bias = "Bullish" if change > 0.45 else "Bearish" if change < -0.45 else "Neutral"
        quotes.append(AssetQuote(symbol=symbol, name=name, price=price, change_percent=change, confidence=random.randint(62, 91), bias=bias))
    return quotes


def candle_history(symbol: str, points: int = 96) -> list[dict[str, float | str]]:
    random.seed(symbol)
    base = 1400 if symbol == "R_100" else 900
    rows = []
    price = base
    for point in range(points):
        open_price = price
        close_price = open_price + random.uniform(-10, 12)
        high = max(open_price, close_price) + random.uniform(1, 8)
        low = min(open_price, close_price) - random.uniform(1, 8)
        price = close_price
        rows.append(
            {
                "time": point,
                "open": round(open_price, 2),
                "high": round(high, 2),
                "low": round(low, 2),
                "close": round(close_price, 2)
            }
        )
    return rows

