from flask import render_template
from task import app, db
from task.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")