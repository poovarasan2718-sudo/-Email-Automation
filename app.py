from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# 🔐 CHANGE THESE
EMAIL_ADDRESS = "poovarasan2718@gmail.com"
EMAIL_PASSWORD = "eqgxcrwpkzehcygn"  


def send_email(to_email, subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        # ✅ Correct SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return True, "Email sent successfully!"

    except Exception as e:
        print("ERROR:", e)
        return False, str(e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()

    to_email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    success, msg = send_email(to_email, subject, message)

    return jsonify({"success": success, "message": msg})


if __name__ == "__main__":
    app.run(debug=True)