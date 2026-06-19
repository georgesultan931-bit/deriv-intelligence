from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import admin, alerts, auth, markets, signals, strategies, ws
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="AI-powered Deriv market intelligence SaaS API."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(markets.router)
app.include_router(signals.router)
app.include_router(strategies.router)
app.include_router(alerts.router)
app.include_router(admin.router)
app.include_router(ws.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy", "service": "deriv-intelligence-api"}

