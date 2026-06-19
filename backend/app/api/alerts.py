from fastapi import APIRouter

from app.schemas import AlertCreate

router = APIRouter(prefix="/alerts", tags=["alerts"])

ALERTS: list[dict[str, object]] = []


@router.post("")
def create_alert(payload: AlertCreate) -> dict[str, object]:
    alert = payload.model_dump()
    alert["id"] = len(ALERTS) + 1
    alert["status"] = "armed"
    ALERTS.append(alert)
    return alert


@router.get("")
def list_alerts() -> dict[str, object]:
    return {"alerts": ALERTS}

