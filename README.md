# contact-mail-api
This application provides a route for users to submit their contact information, including name, email, and a message. The server validates the email address, ensures the form is filled correctly, verifies the reCAPTCHA response, and sends the contact message via email.

## Setup
Follow these steps to run it locally:
```
git clone https://github.com/araujo2kg/contact-mail-api.git
cd contact-mail-api
```

```
python3 -m venv .venv
Windows: .venv\Scripts\activate
Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```
Create a .env file and set the data in the brackets (<>)
```
PORT=5000
ORIGINS=http://127.0.0.1
RECAPTCHA_KEY=<your-recaptcha-secret-key>
RECAPTCHA_URL=https://www.google.com/recaptcha/api/siteverify
MAIL_HOST=smtp.gmail.com
MAIL_PORT=465
MAIL_SECURE=true
MAIL_AUTH_USER=<staff@example.com>
MAIL_AUTH_PASS=<your-email-password>
TEXT_MAIL_TITLE=Contact form
TEXT_MAIL_BODY=Contact from {name}, using mail: {email}, about: {comment}
TEXT_MAIL_HTML=Contact from {name}, using mail: {email}, about: {comment}
``` 
Run with:
```
flask --app app run --debug
```

## Testing
You can test it at https://contact-mail-api-03mn.onrender.com/contact, by running locally and navigating to the /contact route and sending the form or generating a recaptcha token and making a direct post request.
