# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the current valid password
valid_password = "October2024Pass"


@app.route('/verify-password', methods=['POST'])
def verify_password():
    password = request.form['password']

    if password == valid_password:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failure"}), 401


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
