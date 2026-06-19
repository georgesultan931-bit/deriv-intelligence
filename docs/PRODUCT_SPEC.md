# Deriv Intelligence Product Specification

## Vision

Deriv Intelligence is a premium SaaS analysis terminal for Deriv traders. It combines real-time market streaming, technical indicators, explainable AI insights, signal management, custom strategy building, alerting, subscriptions, and admin operations in one commercial-grade platform.

## Product Pillars

- Real-time trading intelligence.
- Explainable AI analysis.
- Professional technical-analysis workflows.
- Subscription-ready SaaS operations.
- Responsive fintech terminal experience.

## User Roles

- Visitor: can view marketing/auth screens.
- Trader: can use dashboard, charts, watchlists, alerts, and saved strategies.
- Pro Trader: can access AI insights, signals, backtests, and advanced reports.
- Admin: can manage users, plans, subscriptions, analytics, and system status.

## MVP

- Authentication scaffolding.
- Main dashboard.
- Live market overview with WebSocket mock feed.
- Technical-analysis indicators.
- AI insight endpoint.
- Signal center.
- Strategy builder data model and API.
- Alert rules.
- Admin overview.
- Docker deployment.

## Production Roadmap

1. Replace mock feed with Deriv WebSocket app connection.
2. Add persistent auth with email verification and password reset.
3. Add Stripe/Paddle billing.
4. Add PostgreSQL migrations and background workers.
5. Train and deploy model versions for volatility, trend, and reversal detection.
6. Add mobile push notifications.
7. Add full historical backtesting workers.

