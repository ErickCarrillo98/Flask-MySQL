from flask import render_template, request, session, redirect

from flask_app import app
from ..models.user import User
from ..models.collar import Collar

@app.route("/collars/new")
def new_collar_form():
    return render_template("new_collar.html", all_users = User.get_all_users())


@app.route("/collars/create", methods = ['POST'])
def create_collar():
    Collar.create(request.form)
    
    return redirect("/")


@app.route("/collar/<int:collar_id>")
def show_collar(collar_id):
    return render_template("show_collar.html", collar = Collar.get_one_collar({'id': collar_id}))