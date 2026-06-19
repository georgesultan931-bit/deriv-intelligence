from app.schemas import Signal


def build_signal(asset: str, latest_price: float, insight: dict[str, object]) -> Signal:
    trend = insight["technicals"]["trend"]  # type: ignore[index]
    side = "Buy" if trend == "Bullish" else "Sell"
    risk = str(insight["risk"])
    confidence = int(insight["confidence"])
    stop_distance = latest_price * (0.012 if risk == "High" else 0.008)
    target_distance = stop_distance * 1.8
    return Signal(
        asset=asset,
        side=side,
        entry=round(latest_price, 2),
        stop_loss=round(latest_price - stop_distance if side == "Buy" else latest_price + stop_distance, 2),
        take_profit=round(latest_price + target_distance if side == "Buy" else latest_price - target_distance, 2),
        confidence=confidence,
        risk=risk,
        reason=str(insight["summary"])
    )

