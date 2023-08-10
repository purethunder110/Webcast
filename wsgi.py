from flask import Flask,render_template,request
from ytcast import search_vids,id_data_creater,YouTube

app=Flask(__name__)


queue=[]
websites=["About","Devices","Search","playlist"]
yt_data=dict()

@app.route('/')
def homepage():
    queue=send_data=[]
    return render_template("about.html",title="About",websites=websites)

@app.route('/search',methods=['GET','POST'])
def searchpage():
    if request.method=="POST":
        #getting the search result
        search_term=request.form['search_term']
        queue=search_vids(search_term)
        #creating YT object for getting title and link etc
        yt_data=id_data_creater(queue)
        return render_template('about.html',title="Search",websites=websites,yt_data=yt_data,queue=queue)

    return render_template('about.html',title="Search",websites=websites)