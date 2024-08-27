import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(receiver_email, subject, text_message):
    sender_email = "0786indianking@gmail.com"
    password = "CHANGE_LATER"

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    html = f"""\
    <html>
    <body>
    <h1 style="color: red;">{subject}</h1>
        <p>{text_message}</p>
    </body>
    </html>
    """

    template = MIMEText(html, "html")
    message.attach(template)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )