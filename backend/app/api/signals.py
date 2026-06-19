from fastapi import APIRouter

from app.services.ai_analysis import generate_insight
from app.services.market import ASSETS, candle_history
from app.services.signals import build_signal

router = APIRouter(prefix="/signals", tags=["signals"])


@router.get("/live")
def live_signals() -> dict[str, object]:
    output = []
    for symbol in ASSETS:
        rows = candle_history(symbol)
        closes = [float(row["close"]) for row in rows]
        insight = generate_insight(closes, symbol)
        output.append(build_signal(symbol, closes[-1], insight).model_dump())
    return {"signals": output}


@router.get("/history")
def signal_history() -> dict[str, object]:
    return {"history": [], "message": "Persisted signal history is ready for database integration."}

