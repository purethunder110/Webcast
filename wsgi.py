from flask import Flask,render_template

app=Flask(__name__)



websites=["About","Devices","Search","playlist"]
yt_id=[]

@app.route('/')
def homepage():
    return render_template("about.html",title="About",websites=websites)

@app.route('/search/',methods=('GET','POST'))
def searchpage():
    return render_template('about.html',title="Search",websites=websites)