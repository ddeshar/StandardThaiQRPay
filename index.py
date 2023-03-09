import json
import base64
import qrcode
import time
from flask import Flask, jsonify, request, make_response
from promptpay import qrcode

# Create a Flask application object
app = Flask(__name__)

# Load the data from the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Define a route for the endpoint that generates the QR code
@app.route('/generateQR', methods=['POST', 'GET'])
def generateQR():
    # Initialize the amount to 0
    amount = 0

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the JSON data from the request
        req_data = request.get_json()
        # If the request data is None, return a bad request error
        if req_data is None:
            return jsonify({
                "RespCode": 400,
                "RespMessage": "Bad Request",
                "Result": "Request body must be in JSON format"
            }), 400
        # Get the amount from the request data
        amount = float(req_data.get("amount", 0))
    # Check if the request method is GET
    elif request.method == 'GET':
        # Get the amount from the query parameters
        amount = float(request.args.get('amount', 0))
    # If the request method is not supported, return a bad request error
    else:
        return jsonify({
            "RespCode": 400,
            "RespMessage": "Bad Request",
            "Result": "HTTP method not supported"
        }), 400
        
    # Set the mobile number for the payment
    mobileNumber = '0840868074'
    # Generate the QR code payload with the mobile number and amount
    payload = qrcode.generate_payload(mobileNumber, amount=amount)
    # Create the QR code image from the payload
    img = qrcode.to_image(payload)
    # Get the current timestamp as a string
    timestamp = str(int(time.time()))
    # Create a unique filename for the QR code image
    filename = f'qrcode_{timestamp}.png'
    # Save the QR code image to a file
    img.save(filename)
    # Open the QR code image file
    with open(filename, 'rb') as f:
        # Read the image data from the file
        image_data = f.read()
    # Create a Flask response object with the image data
    response = make_response(image_data)
    # Set the content type of the response to image/png
    response.headers.set('Content-Type', 'image/png')
    # Return the response
    return response

# If this script is being run as the main program, start the Flask application
if __name__ == '__main__':
    app.run(port=3000, debug=True)
