from flask import Flask,render_template

app=Flask(__name__)


websites=["About","Devices","search","playlist"]

@app.route('/')
def homepage():
    return render_template("about.html",
                           title="About",
                           websites=websites)