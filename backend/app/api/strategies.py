from fastapi import APIRouter

from app.schemas import StrategyCreate

router = APIRouter(prefix="/strategies", tags=["strategies"])

SAVED_STRATEGIES: list[dict[str, object]] = []


@router.post("")
def create_strategy(payload: StrategyCreate) -> dict[str, object]:
    strategy = payload.model_dump()
    strategy["id"] = len(SAVED_STRATEGIES) + 1
    strategy["status"] = "active"
    SAVED_STRATEGIES.append(strategy)
    return strategy


@router.get("")
def list_strategies() -> dict[str, object]:
    return {"strategies": SAVED_STRATEGIES}


@router.post("/{strategy_id}/backtest")
def backtest(strategy_id: int) -> dict[str, object]:
    return {
        "strategy_id": strategy_id,
        "trades": 128,
        "win_rate": 64.8,
        "profit_factor": 1.74,
        "max_drawdown": 8.2,
        "sharpe": 1.41
    }

