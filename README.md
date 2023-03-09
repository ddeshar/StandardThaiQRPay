# StandardThaiQRPay
StandardQRPay: A Flask-Powered PromptPay QR Code Generator"

# QR Code Generator for PromptPay Payments with StandardQR Code

This project is a sample app that generates QR codes for PromptPay payments utilizing the StandardQR Code specification. The code is written in Python and utilizes the Flask framework. The app allows you to input an amount and a mobile number to generate a QR code that can be scanned for payment.

StandardQR Code is a Thai national QR code standard for financial transactions developed by the Bank of Thailand. This standard is intended to increase the interoperability of QR code payments in Thailand and promote the use of mobile payments.

## Installation

To run this project, you will need to have Python 3.x and Flask installed. 

Use the following command to install the dependencies:

```pip install -r requirements.txt```


## Usage

To run the app, use the following command:

```python index.py```


The app will be available at `http://localhost:3000/`. You can access the QR code generator by sending a GET or POST request to `http://localhost:3000/generateQR`. The amount parameter should be passed as a float in the request body or as a query string parameter. 

## Contributing

If you would like to contribute to this project, please create a pull request with a detailed explanation of your changes.

## License

This project is licensed under the MIT License.
