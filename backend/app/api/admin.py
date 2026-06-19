from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/overview")
def admin_overview() -> dict[str, object]:
    return {
        "users": 1240,
        "active_subscriptions": 416,
        "monthly_recurring_revenue": 18240,
        "signals_generated_today": 392,
        "system_status": {
            "api": "healthy",
            "websocket": "healthy",
            "worker": "healthy",
            "deriv_feed": "mock-ready"
        }
    }

