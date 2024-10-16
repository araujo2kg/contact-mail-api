from flask import Flask, request, render_template
from helper import (
    validate_recaptcha,
    get_request_data,
    create_error_response,
    send_email,
)
from dotenv import load_dotenv
import os
from email_validator import validate_email, EmailNotValidError


load_dotenv()
app = Flask(__name__)


@app.route("/contact", methods=("GET", "POST"))
def contact():
    if request.method == "GET":
        return render_template("form.html")

    data = get_request_data(request)
    if validate_recaptcha(data.get("g-recaptcha-response")):

        # Check name
        name = data.get("name")
        if not name:
            return (
                create_error_response(title="BadRequestError", detail="Empty name"),
                400,
            )

        # Check email
        try:
            email = validate_email(data.get("email"), check_deliverability=True)
        except EmailNotValidError as error:
            return (
                create_error_response(
                    title="BadRequestError", detail=f"Invalid email: {str(error)}"
                ),
                400,
            )

        # Send email
        try:
            send_email(
                os.getenv("MAIL_AUTH_USER"), email.normalized, name, data.get("comment")
            )
        except Exception:
            return create_error_response(), 500

        return "", 201
    else:
        return (
            create_error_response(
                title="UnauthorizedError", detail="Incorrect captcha"
            ),
            401,
        )


if __name__ == "__main__":
    app.run(debug=True)
