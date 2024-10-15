from flask import jsonify

def validate_recaptcha(response_token):
    pass


def get_request_data(request):
    if request.is_json:
        return request.get_json()
    else: 
        return request.form.to_dict()

        
def create_error_response(type="about:blank", title="InternalServerError", detail="Server error", instance="/contact"):
    return jsonify({
        "type": type,
        "title": title,
        "detail": detail,
        "instance": instance,
    })


