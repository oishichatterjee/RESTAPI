from flask import Flask, request, jsonify
from flask_cors import CORS
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Replace these with your actual details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

def is_valid_json(data):
    return isinstance(data, dict) and "data" in data and isinstance(data["data"], list)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json
        
        if not is_valid_json(data):
            return jsonify({"is_success": False}), 400

        numbers = []
        alphabets = []
        highest_lowercase = []

        for item in data["data"]:
            if item.isdigit():
                numbers.append(item)
            elif len(item) == 1 and item.isalpha():
                alphabets.append(item)
                if item.islower():
                    highest_lowercase = [max(highest_lowercase + [item])] if highest_lowercase else [item]

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }

        return jsonify(response)

    elif request.method == 'GET':
        return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)