from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class PasswordResetRequest(BaseModel):
    email: EmailStr


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str = "trader"


class AssetQuote(BaseModel):
    symbol: str
    name: str
    price: float
    change_percent: float
    confidence: int
    bias: str


class Signal(BaseModel):
    asset: str
    side: str
    entry: float
    stop_loss: float
    take_profit: float
    confidence: int
    risk: str
    reason: str


class StrategyRule(BaseModel):
    indicator: str
    operator: str
    value: str


class StrategyCreate(BaseModel):
    name: str
    asset: str
    timeframe: str
    rules: list[StrategyRule]


class AlertCreate(BaseModel):
    asset: str
    condition: str
    target_price: float
    channel: str = "email"
