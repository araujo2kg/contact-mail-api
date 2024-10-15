import os
import requests
from flask import jsonify


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
