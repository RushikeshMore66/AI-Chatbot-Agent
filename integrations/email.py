import smtplib
from email.mime.text import MIMEText
from config import EMAIL_USER, EMAIL_PASS

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        return f"Email sent to {to}"
    except Exception as e:
        return str(e)