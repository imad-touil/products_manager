from flask import Flask


# Create first Flask Application
product_manager = Flask(__name__)

# Add routes // route ==>> massar 
@product_manager.route("/") # main route for example : imadtouil.com

# function that return home page requiste
def home():
    return "Hello world"


# Creating more Route
@product_manager.route("/about")


def about():
    return "Aout US"

if __name__ == '__main__':
    product_manager.run(debug=True, port=9000)
