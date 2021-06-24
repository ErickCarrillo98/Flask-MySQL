from flask import render_template, request, session, redirect

from flask_app import app
from ..models.dojo import Dojo




@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("index.html", all_dojos = dojos)


@app.route("/dojos/create", methods = ['POST'])
def create_dojo():

    Dojo.create(request.form)

    return redirect("/")


@app.route("/dojo/<int:dojo_id>")
def show_dojo(dojo_id):
    dojoNinjas = Dojo.get_one({'id': dojo_id})

    return render_template("show_dojo.html", dojo = dojoNinjas)

