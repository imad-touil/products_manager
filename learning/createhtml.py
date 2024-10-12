from flask import Flask, render_template

create_app = Flask(__name__)

@create_app.route("/")

def home():
    return render_template("homepage.html", pagetitle="homepage")

@create_app.route("/about")

def aboutpage():
    return render_template("about.html", pagetitle="about us")


if __name__ == "__main__":
    create_app.run(debug=True, port=9000)