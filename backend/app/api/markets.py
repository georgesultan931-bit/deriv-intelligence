from fastapi import APIRouter

from app.services.ai_analysis import generate_insight
from app.services.market import candle_history, current_quotes
from app.services.signals import build_signal

router = APIRouter(prefix="/markets", tags=["markets"])


@router.get("/overview")
def overview() -> dict[str, object]:
    return {"assets": [quote.model_dump() for quote in current_quotes()]}


@router.get("/{symbol}/candles")
def candles(symbol: str) -> dict[str, object]:
    rows = candle_history(symbol)
    return {"symbol": symbol, "candles": rows}


@router.get("/{symbol}/analysis")
def analysis(symbol: str) -> dict[str, object]:
    rows = candle_history(symbol)
    closes = [float(row["close"]) for row in rows]
    return generate_insight(closes, symbol)


@router.get("/{symbol}/signal")
def signal(symbol: str) -> dict[str, object]:
    rows = candle_history(symbol)
    closes = [float(row["close"]) for row in rows]
    insight = generate_insight(closes, symbol)
    return build_signal(symbol, closes[-1], insight).model_dump()

