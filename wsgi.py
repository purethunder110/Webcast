from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def homepage():
    return render_template("about.html",
                           title="this is a test title")