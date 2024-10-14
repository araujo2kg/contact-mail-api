def validate_recaptcha():
    pass


def get_request_data(request):
    if request.is_json:
        return request.get_json()
    else: 
        return request.form.to_dict()

        
def create_error_response():
    pass


