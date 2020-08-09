from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/about/<name>/<int:user_id>')
def display_about(name, user_id):
    return render_template("about.html", name=name, user_id=user_id)
