from flask import render_template, request, session, redirect

from flask_app import app

from ..models.user import User
from ..models.recipe import Recipe



@app.route("/dashboard")
def dashboard():
    if "uuid" not in session:
        return redirect ("/")

    return render_template("dashboard.html", user = User.get_by_id({"id": session['uuid']}))


@app.route("/recipes/new")
def new_recipe():
    if "uuid" not in session:
        return redirect ("/")

    return render_template("new_recipe.html")


@app.route("/recipes/create", methods = ['POST'])
def create_recipe():
    if not Recipe.validate(request.form):
        return redirect("/recipes/new")

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "user_id": session['uuid']
    }
    Recipe.create(data)

    return redirect("/dashboard")


@app.route("/recipes/<int:id>/edit")
def edit_recipe(id):
    if "uuid" not in session:
        return redirect ("/")

    return render_template("edit_recipe.html", recipe = Recipe.get_one({"id": id}))



@app.route("/recipes/<int:id>/update", methods = ['POST'])
def update_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f"/recipes/{id}/edit")
    
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "id": id
    }

    Recipe.update(data)

    return redirect("/dashboard")



@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    Recipe.delete({"id": id})

    return redirect("/dashboard")


@app.route("/recipes/<int:id>")
def display_recipe(id):
    if "uuid" not in session:
        return redirect ("/")

    return render_template("recipe.html", user = User.get_by_id({"id": session['uuid']}),
    recipe = Recipe.get_one({"id": id})
    )


