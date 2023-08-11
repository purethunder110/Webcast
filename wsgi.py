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
def searchpage(queue=[]):
    if 'search_term' in request.form:
        #getting the search result
        search_term=request.form['search_term']
        queue=search_vids(search_term)
        #creating YT object for getting title and link etc
        yt_data=id_data_creater(queue)
        print("is this stuck?")
        return render_template('search.html',title="Search",websites=websites,yt_data=yt_data,queue=queue)
    else:
        print(str(request.form)[-15:-4])

    return render_template('search.html',title="Search",websites=websites)