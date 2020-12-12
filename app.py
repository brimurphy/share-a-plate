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
    users = mongo.db.users.find().sort("username", 1)
    return render_template("index.html", users=users)


# all registered users
@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    users = mongo.db.users.find().sort("username", 1)
    return render_template("recipes.html", recipes=recipes, users=users)


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


# registered users
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    recipes = list(mongo.db.recipes.find())
    users = mongo.db.users.find().sort("username", 1)

    if session["user"]:
        return render_template(
            "my_recipes.html", username=username, recipes=recipes, users=users)

    return redirect(url_for("login"))


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    recipe_id = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)}
        )
    recipes = list(mongo.db.recipes.find(recipe_id))
    users = mongo.db.users.find().sort("username", 1)
    return render_template(
        "full_recipe.html", recipe=recipe_id, recipes=recipes, users=users)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    users = list(mongo.db.users.find().sort("username", 1))
    if request.method == "POST":
        recipe = {
            "diet": request.form.get("diet"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_img": request.form.get("recipe_img"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "username": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added, Thanks for sharing")
        return redirect(url_for("my_recipes", username=username))
    diets = mongo.db.diets.find().sort("diet", 1)
    return render_template("add_recipe.html", diets=diets, users=users)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if request.method == "POST":
        update = {
            "diet": request.form.get("diet"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_img": request.form.get("recipe_img"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "username": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update)
        flash("Recipe has been Updated")
        return redirect(url_for("my_recipes", username=username))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    diets = mongo.db.diets.find().sort("diet", 1)
    return render_template("edit_recipe.html", recipe=recipe, diets=diets)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe has been Deleted")
    return redirect(url_for("my_recipes", username=username))


@app.route("/logout")
def logout():
    flash("You've Successfully Logged Out")
    # use pop instead of clear as affects flash msg
    session.pop("user")
    return redirect(url_for("login"))


# admin users
@app.route("/admin_page")
def admin_page():
    users = list(mongo.db.users.find().sort("username", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    diets = mongo.db.diets.find().sort("diet", 1)
    return render_template(
        "admin_page.html", users=users, recipes=recipes, diets=diets)


@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        update = {
            "is_superuser": request.form.get("edit_user")
        }
        mongo.db.users.update({"_id": ObjectId(user_id)}, update)
        flash("User Updated")
        return redirect(url_for("admin_page"))
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_user.html", user=user)


@app.route("/add_diet", methods=["GET", "POST"])
def add_diet():
    if request.method == "POST":
        diet = {
            "diet": request.form.get("diet_name")
        }
        mongo.db.diets.insert_one(diet)
        flash("New Diet Added")
        return redirect(url_for("admin_page"))

    return render_template("add_diet.html")


@app.route("/edit_diet/<diet_id>", methods=["GET", "POST"])
def edit_diet(diet_id):
    if request.method == "POST":
        update = {
            "diet": request.form.get("edit_diet")
        }
        mongo.db.diets.update({"_id": ObjectId(diet_id)}, update)
        flash("Diet Updated")
        return redirect(url_for("admin_page"))
    diet = mongo.db.diets.find_one({"_id": ObjectId(diet_id)})
    return render_template("edit_diet.html", diet=diet)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
