from app.services.technical_analysis import analyze, bollinger_bands, rsi


def test_rsi_returns_number() -> None:
    values = [100, 101, 99, 102, 105, 104, 106, 108, 107, 109, 111, 110, 112, 114, 113]
    assert 0 <= rsi(values) <= 100


def test_bollinger_bands_are_ordered() -> None:
    values = [float(value) for value in range(100, 130)]
    bands = bollinger_bands(values)
    assert bands["upper"] > bands["middle"] > bands["lower"]


def test_analyze_returns_trend() -> None:
    values = [float(value) for value in range(100, 160)]
    result = analyze(values)
    assert result["trend"] in {"Bullish", "Bearish"}
