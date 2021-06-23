from flask import render_template, request, session, redirect
from flask_bcrypt import Bcrypt

from flask_app import app

from ..models.user import User

bcrypt = Bcrypt(app)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/register", methods = ["POST"])
def register():
    if not User.register_validator(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }

    user_id = User.create(data)

    session['uuid'] = user_id

    return redirect("/success")


@app.route("/login", methods = ["POST"])
def login():
    if not User.login_validator(request.form):
        return redirect("/")

    user = User.get_by_email({"email": request.form['email']})

    session['uuid'] = user.id

    return redirect("/success")


@app.route("/success")
def success():
    return render_template("success.html", user = User.get_by_id({"id": session['uuid']}))


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")
