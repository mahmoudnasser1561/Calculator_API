# Flask Calculator API

## OverView
Calculator_API is a simple yet fully functional RESTful API built with Flask that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

It accepts HTTP POST requests with JSON payload or URL query parameters, performs calculations, and returns JSON responses with the results.

This project demonstrates:
- REST API design and development
- JSON request handling and validation
- Separation of concerns between API endpoints and business logic
- Error handling and response status codes
- Deployment readiness on cloud platforms like AWS

## Features
- Add, Subtract, Multiply, Divide via /add, /subtract, /multiply, /divide endpoints
- Accepts data in both JSON body and URL query parameters
- Proper error handling for invalid inputs 
- Clear and consistent JSON responses with status codes
- Easily extendable to add more operations or features

## Getting Started
### Prequisites
- Python 3.8 or higher
- pip for Python package management
- (Optional) Virtual environment tool such as venv

### Installation
- Clone the repository:
  ```
  git clone https://github.com/mahmoudnasser1561/Calculator_API.git
  cd Calculator_API
  ```
- Create and activate a virtual environment (recommended):
  ```
  python3 -m venv venv
  source venv/bin/activate  # Linux/Mac
  ```
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```
  ## Running the API locally
  ### Start the Flask development server:
  ```
  python3 app.py
  ```
  ### By default, the server runs at:
  ```
  http://127.0.0.1:5000/

  ```

  ## API Usage
  #### Add
  #### POST /add
  #### Request Body (JSON):
  ```
  {
  "x": 5,
  "y": 3
  }
  
  ```
  #### Response
  ```
  {
  "Message": 8,
  "Status Code": 200
  }
  
  ```

