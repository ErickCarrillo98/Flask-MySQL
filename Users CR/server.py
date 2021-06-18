from flask import Flask, render_template, request, session, redirect

from user import User

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."


@app.route('/')
def index():
    users = User.get_all_users()
    return render_template("index.html", all_users = users)



@app.route("/users/new")
def new_users_form():
    return render_template("new_user.html")


@app.route("/users/create", methods = ["POST"])
def create_user():
    print(request.form)
    User.create(request.form)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)
