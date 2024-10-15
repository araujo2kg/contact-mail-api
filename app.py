from flask import Flask, request, render_template
from helper import validate_recaptcha, get_request_data, create_error_response

app = Flask(__name__)

@app.route("/contact", methods=("GET", "POST"))
def contact():
    if request.method == "GET":
        return render_template("form.html")

    data = get_request_data(request)
    if validate_recaptcha(data.get("g-recaptcha-response")):
        # Validate the rest of the data
        pass
    else:
        return create_error_response(title="UnauthorizedError", detail="Incorrect captcha") 
    




if __name__ == "__main__":
    app.run(debug=True)