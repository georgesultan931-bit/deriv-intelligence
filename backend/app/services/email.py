from email.message import EmailMessage
import smtplib
import ssl

from app.core.config import get_settings


def send_email(to_email: str, subject: str, body: str) -> dict[str, str]:
    settings = get_settings()
    if not settings.email_host_user or not settings.email_host_password:
        return {"status": "skipped", "reason": "SMTP credentials are not configured"}

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = settings.default_from_email or settings.email_host_user
    message["To"] = to_email
    message.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP(settings.email_host, settings.email_port, timeout=20) as server:
        if settings.email_use_tls:
            server.starttls(context=context)
        server.login(settings.email_host_user, settings.email_host_password)
        server.send_message(message)

    return {"status": "sent"}


def send_verification_email(to_email: str, token: str) -> dict[str, str]:
    settings = get_settings()
    verify_url = f"{settings.frontend_url}/verify-email?token={token}"
    return send_email(
        to_email,
        "Verify your Deriv Intelligence account",
        (
            "Welcome to Deriv Intelligence.\n\n"
            f"Verify your email using this link:\n{verify_url}\n\n"
            "If you did not create this account, ignore this email."
        )
    )


def send_password_reset_email(to_email: str, token: str) -> dict[str, str]:
    settings = get_settings()
    reset_url = f"{settings.frontend_url}/reset-password?token={token}"
    return send_email(
        to_email,
        "Reset your Deriv Intelligence password",
        (
            "We received a password reset request for your Deriv Intelligence account.\n\n"
            f"Reset your password here:\n{reset_url}\n\n"
            "If you did not request this, you can ignore this email."
        )
    )
