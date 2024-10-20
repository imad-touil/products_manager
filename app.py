from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html",
                           title="product manager",
                           custom_css="index")

@app.route("/products")
def broducts():
    return render_template("products.html", title="صفحة المنتجات", custom_css="products")





if (__name__ == "__main__"):
    app.run(debug=True, port=9000)
    