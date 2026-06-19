# Deriv Intelligence

Premium SaaS market analysis platform for Deriv traders.

## Apps

- `frontend` - Next.js + Tailwind fintech terminal UI.
- `backend` - FastAPI API, authentication scaffolding, market analysis, signals, and WebSocket streaming.
- `infra` - Docker Compose and deployment examples.

## Quick Start

```bash
cd "C:\Users\SULTAN\Desktop\Deriv Intelligence"
docker compose up --build
```

Frontend: http://localhost:3000  
Backend API: http://localhost:8000/docs

## Local Development

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

```bash
cd frontend
npm install
npm run dev
```

## Environment

Copy `.env.example` to `.env` in the root or app folders and fill production secrets.

This scaffold includes realistic mocks where external services are needed. Replace the mock market feed with real Deriv API app credentials before production launch.
