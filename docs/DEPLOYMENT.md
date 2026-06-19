# Deployment Guide

## Best Production Path

Use this setup for a real public deployment:

- Frontend: Vercel
- Backend API: Render Web Service
- Database: Render PostgreSQL
- Cache/queue: Upstash Redis or Render Redis
- Domain: Cloudflare or your domain registrar

## 1. Push Project To GitHub

From the project root:

```bash
git init
git add .
git commit -m "Initial Deriv Intelligence platform"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/deriv-intelligence.git
git push -u origin main
```

## 2. Deploy Backend To Render

Option A: Blueprint deployment

1. Open Render.
2. Choose New Blueprint.
3. Connect the GitHub repository.
4. Select `infra/render.yaml`.
5. Create services.

Option B: Manual backend deployment

1. Create a new Web Service.
2. Root directory: `backend`
3. Build command:

```bash
pip install -r requirements.txt
```

4. Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

5. Add environment variables:

```env
JWT_SECRET=replace-with-a-long-random-secret
FRONTEND_URL=https://your-vercel-domain.vercel.app
DATABASE_URL=your-render-postgres-url
REDIS_URL=your-redis-url
DERIV_APP_ID=your-deriv-app-id
DERIV_API_TOKEN=your-deriv-token
```

Backend health check:

```text
https://your-render-api.onrender.com/health
```

API docs:

```text
https://your-render-api.onrender.com/docs
```

## 3. Deploy Frontend To Vercel

1. Open Vercel.
2. Import the same GitHub repository.
3. Set root directory to `frontend`.
4. Add environment variables:

```env
NEXT_PUBLIC_API_URL=https://your-render-api.onrender.com
NEXT_PUBLIC_WS_URL=wss://your-render-api.onrender.com
```

5. Deploy.

Frontend URL:

```text
https://your-vercel-domain.vercel.app
```

## 4. Local Docker Deployment

Docker is not installed on this machine right now. Once Docker Desktop is installed, run:

```bash
cd "C:\Users\SULTAN\Desktop\Deriv Intelligence"
docker compose up --build
```

Services:

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## 5. Manual Local Development

Backend:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## Production Checklist

- Replace simulated market data with real Deriv WebSocket API.
- Move demo in-memory auth into PostgreSQL tables.
- Add migrations with Alembic.
- Add Stripe or Paddle subscription webhooks.
- Add background workers for signals, alerts, and backtests.
- Add Sentry or OpenTelemetry monitoring.
- Add TLS, secure cookies, and production CORS origins.
- Run load tests for WebSocket tick streaming.
