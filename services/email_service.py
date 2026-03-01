import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(receiver_email: str, pdf_file: str, patient_name: str):

    sender_email = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not email_password:
        raise ValueError("Email credentials not set in environment variables.")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Your Vitiligo Assessment Report"

    body = f"Hello {patient_name},\n\nPlease find your attached Vitiligo Assessment Report.\n\nRegards."
    msg.attach(MIMEText(body, "plain"))

    with open(pdf_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(pdf_file)}"
        )
        msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, email_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()