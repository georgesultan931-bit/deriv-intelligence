from app.services.technical_analysis import analyze


def generate_insight(values: list[float], asset: str) -> dict[str, object]:
    technicals = analyze(values)
    trend = technicals["trend"]
    rsi = float(technicals["rsi_14"])
    volatility = float(technicals["volatility"])
    confidence = 62

    if trend == "Bullish":
        confidence += 12
    if 45 <= rsi <= 68:
        confidence += 10
    if volatility > 5:
        confidence += 6

    confidence = min(confidence, 94)
    risk = "High" if volatility > 9 or rsi > 75 else "Medium" if volatility > 5 else "Low"

    return {
        "asset": asset,
        "summary": f"{asset} shows a {trend.lower()} technical profile with RSI at {rsi} and volatility at {round(volatility, 2)}.",
        "confidence": confidence,
        "risk": risk,
        "reasons": [
            f"Fast EMA structure is {trend.lower()}.",
            "RSI is within tradable range." if 35 <= rsi <= 70 else "RSI is close to exhaustion.",
            "Volatility is sufficient for short-term opportunity." if volatility > 5 else "Volatility is compressed."
        ],
        "technicals": technicals
    }

