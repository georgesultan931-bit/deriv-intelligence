from secrets import token_urlsafe

from fastapi import APIRouter, HTTPException

from app.core.security import create_access_token, hash_password, verify_password
from app.schemas import AuthResponse, LoginRequest, PasswordResetRequest, RegisterRequest
from app.services.email import send_password_reset_email, send_verification_email

router = APIRouter(prefix="/auth", tags=["auth"])

DEMO_USERS: dict[str, dict[str, str]] = {}
EMAIL_TOKENS: dict[str, str] = {}
RESET_TOKENS: dict[str, str] = {}


@router.post("/register", response_model=AuthResponse)
def register(payload: RegisterRequest) -> AuthResponse:
    if payload.email in DEMO_USERS:
        raise HTTPException(status_code=409, detail="Account already exists")

    verification_token = token_urlsafe(32)
    DEMO_USERS[payload.email] = {
        "full_name": payload.full_name,
        "password": hash_password(payload.password),
        "role": "trader",
        "email_verified": "false"
    }
    EMAIL_TOKENS[verification_token] = payload.email
    send_verification_email(payload.email, verification_token)
    return AuthResponse(access_token=create_access_token(payload.email), role="trader")


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest) -> AuthResponse:
    user = DEMO_USERS.get(payload.email)
    if not user or not verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return AuthResponse(access_token=create_access_token(payload.email, user["role"]), role=user["role"])


@router.post("/password-reset")
def password_reset(payload: PasswordResetRequest) -> dict[str, str]:
    reset_token = token_urlsafe(32)
    RESET_TOKENS[reset_token] = payload.email
    email_status = send_password_reset_email(payload.email, reset_token)
    return {"status": "queued", "email_status": email_status["status"]}


@router.post("/verify-email")
def verify_email(token: str) -> dict[str, str]:
    email = EMAIL_TOKENS.pop(token, None)
    if not email or email not in DEMO_USERS:
        raise HTTPException(status_code=400, detail="Invalid or expired verification token")
    DEMO_USERS[email]["email_verified"] = "true"
    return {"status": "verified"}
