from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

ADMIN_EMAIL = "aniketsingh333u@gmail.com"  # Change this to your admin's email
GMAIL_USER = "your-email@gmail.com"
GMAIL_PASS = "your-app-password"  # Use App Password (if 2FA enabled)

def send_email(name, email, phone, dob, address):
    msg = EmailMessage()
    msg['Subject'] = "New CCC Course Enrollment"
    msg['From'] = GMAIL_USER
    msg['To'] = ADMIN_EMAIL

    msg.set_content(f"""
    A new student has enrolled in the CCC Course.
    
    Name: {name}
    Email: {email}
    Phone: {phone}
    Date of Birth: {dob}
    Address: {address}
    """)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(GMAIL_USER, GMAIL_PASS)
        smtp.send_message(msg)

@app.route('/send-email', methods=['POST'])
def enroll():
    data = request.json
    try:
        send_email(data['name'], data['email'], data['phone'], data['dob'], data['address'])
        return jsonify({"message": "Enrollment email sent to the admin!"}), 200
    except Exception as e:
        return jsonify({"message": "Error sending email", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
