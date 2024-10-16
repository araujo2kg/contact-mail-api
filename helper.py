import os
import requests
from flask import jsonify
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def validate_recaptcha(response_token):
    response = requests.post(
        os.getenv("RECAPTCHA_URL"),
        data={
            "secret": os.getenv("RECAPTCHA_KEY"),
            "response": response_token,
        },
    )
    result = response.json()
    return result["success"]


def get_request_data(request):
    if request.is_json:
        return request.get_json()
    else:
        return request.form.to_dict()


def create_error_response(
    type="about:blank",
    title="InternalServerError",
    detail="Server error",
    instance="/contact",
):
    return jsonify(
        {
            "type": type,
            "title": title,
            "detail": detail,
            "instance": instance,
        }
    )


def send_email(sender, receiver, name, comment):
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = os.getenv("TEXT_MAIL_TITLE")
    message["Date"] = formatdate(localtime=True)

    text = MIMEText(
        os.getenv("TEXT_MAIL_BODY").format(name=name, email=receiver, comment=comment),
        "plain",
    )
    html = MIMEText(
        os.getenv("TEXT_MAIL_HTML").format(name=name, email=receiver, comment=comment),
        "html",
    )
    message.attach(text)
    message.attach(html)
    message = message.as_string()

    with SMTP_SSL(os.getenv("MAIL_HOST"), os.getenv("MAIL_PORT")) as smtp:
        smtp.login(os.getenv("MAIL_AUTH_USER"), os.getenv("MAIL_AUTH_PASS"))
        smtp.sendmail(sender, receiver, message)
        smtp.sendmail(sender, sender, message)
