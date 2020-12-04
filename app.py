import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Create instance of Flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        registered_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        password = request.form.get('password')
        password_confirm = request.form.get('password-confirm')

        # check form fields are unique
        if registered_user:
            flash("Username Already Exists")
            return redirect(url_for("register"))

        elif registered_email:
            flash("Email Already In Use")
            return redirect(url_for("register"))

        # check passwords match
        elif password != password_confirm:
            flash("Passwords Don't Match")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Succesful!")
        return redirect(url_for('my_recipes', username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check user exists in db
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if registered_user:
            # check hash passwords match input
            if check_password_hash(
              registered_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}, what are we cooking today?".format(
                    request.form.get("username").capitalize()))
                return redirect(
                    url_for('my_recipes', username=session["user"]))
            else:
                # passwords don't match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # user doesn't exist in db
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("my_recipes.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You've Successfully Logged Out")
    # use pop instead of clear as affects flash msg
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
