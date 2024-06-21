from flask import Flask, render_template, redirect, request
import ssl
import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Stravecodes:ASh2LeaVounah7pu@strave.3nqbbea.mongodb.net/FF?retryWrites=true&w=majority&appName=Strave", tls=True, tlsAllowInvalidCertificates=True)

db = client["FF"]
collection = db["users"]

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    uid = request.form.get("uid")

    details = {"name":name, "email":email, "uid":uid}
    data_find = {'$or': [{"uid":uid}, {"email": email}]}
    if collection.find_one(data_find):
        already_exists = True
        return render_template("index.html", already_exists=already_exists)
    else:
        collection.insert_one(details)
    return render_template("done.html")

if __name__ == "__main__":
    app.run( debug = True)