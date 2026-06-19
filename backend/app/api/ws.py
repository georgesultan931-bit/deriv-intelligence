import asyncio
import random
from datetime import datetime, timezone

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["websocket"])


@router.websocket("/ws/ticks/{symbol}")
async def ticks(websocket: WebSocket, symbol: str) -> None:
    await websocket.accept()
    price = 1400.0
    try:
        while True:
            price += random.uniform(-2.5, 3.0)
            await websocket.send_json(
                {
                    "symbol": symbol,
                    "price": round(price, 2),
                    "time": datetime.now(timezone.utc).isoformat(),
                    "source": "simulated"
                }
            )
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        return

