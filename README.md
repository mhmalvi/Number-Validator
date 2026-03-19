# Number Validator

A phone number validation web application built with Python Flask. The app provides a clean web interface for validating international phone numbers using the NumVerify API, returning carrier details, line type, location, and validity status.

## Features

- **Phone Number Validation** -- Validate phone numbers against the NumVerify API
- **International Support** -- Validate numbers from any country using country codes
- **Detailed Results** -- Returns carrier name, line type (mobile/landline), location, and formatting info
- **Web Interface** -- Clean HTML form for entering phone numbers and viewing results
- **REST Endpoint** -- POST endpoint for programmatic validation via API calls
- **Validation Logging** -- All validation attempts are logged to file with timestamps

## Tech Stack

- **Backend:** Python 3, Flask
- **API:** NumVerify Phone Number Validation API
- **HTTP Client:** Requests
- **Frontend:** HTML templates (Jinja2)

## Prerequisites

- Python 3.6+
- pip
- NumVerify API key (get one at [numverify.com](https://numverify.com))

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mhmalvi/Number-Validator.git
   cd Number-Validator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask requests
   ```

4. **Update the API key** in `api.py` -- replace the `ACCESS_KEY` value with your NumVerify API key.

5. **Run the application**
   ```bash
   python api.py
   ```

The application will be available at `http://localhost:5000`.

## API Usage

### Web Interface

Navigate to `http://localhost:5000` in your browser to use the validation form.

### POST Endpoint

```bash
curl -X POST http://localhost:5000/validate \
  -d "phone_number=14158586273" \
  -d "country_code=US"
```

**Response:**
```json
{
  "valid": true,
  "number": "14158586273",
  "local_format": "4158586273",
  "international_format": "+14158586273",
  "country_prefix": "+1",
  "country_code": "US",
  "country_name": "United States of America",
  "location": "San Francisco",
  "carrier": "AT&T Mobility LLC",
  "line_type": "mobile"
}
```

## Project Structure

```
api.py            # Flask application and validation logic
templates/        # HTML templates (Jinja2)
logs/             # Validation attempt logs (auto-created)
```

## License

MIT
