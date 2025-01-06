from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

# API configuration constants
URL = "http://apilayer.net/api/validate"
ACCESS_KEY = "f635fdab9871010c18543e5f28d15811"

def validate_phone_number(phone_number, country_code="US"):
    """Validate phone number using NumVerify API"""
    try:
        # Clean the phone number
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        if country_code == "US" and phone_number.startswith('1'):
            phone_number = phone_number[1:]
        
        # Prepare API parameters
        params = {
            "access_key": ACCESS_KEY,
            "number": phone_number,
            "country_code": country_code,
            "format": 1
        }
        
        print(f"Sending request with params: {params}")  # Debug print
        
        # Make the API request
        response = requests.get(URL, params=params)
        print(f"Response status code: {response.status_code}")  # Debug print
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse the response
        data = response.json()
        print(f"API Response: {data}")  # Debug print
        
        # Log the validation attempt
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        with open(os.path.join(log_dir, "phone_validation.log"), "a") as f:
            f.write(f"{datetime.now()} - Number: {phone_number} - Response: {data}\n")
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {str(e)}")  # Debug print
        return {"error": f"API Request Failed: {str(e)}"}
    except Exception as e:
        print(f"General Error: {str(e)}")  # Debug print
        return {"error": f"Validation Failed: {str(e)}"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    try:
        phone_number = request.form.get('phone_number')
        country_code = request.form.get('country_code', 'US')
        
        print(f"Received request - Phone: {phone_number}, Country: {country_code}")  # Debug print
        
        if not phone_number:
            return jsonify({"error": "Phone number is required"}), 400
        
        result = validate_phone_number(phone_number, country_code)
        return jsonify(result)
        
    except Exception as e:
        print(f"Validation Error: {str(e)}")  # Debug print
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure templates directory exists
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
