
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    # Render the home page
    return render_template('index.html')

# Define the order page route
@app.route('/order', methods=['POST'])
def order():
    # Get the order details from the request
    order_details = request.form

    # Render the order confirmation page
    return render_template('order.html', order_details=order_details)

# Define the success page route
@app.route('/success')
def success():
    # Render the success page
    return render_template('success.html')

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
