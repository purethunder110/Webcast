from flask import Flask,render_template,request,redirect,url_for
from ytcast import search_vids,id_data_creater,YouTube

app=Flask(__name__)


queue=[]
websites=["About","Devices","Search","playlist"]
yt_data=dict()



#homepage
@app.route('/')
def homepage():
    queue=send_data=[]
    return render_template("about.html",title="About",websites=websites)


#search page
@app.route('/search',methods=['GET','POST'])
def searchpage(queue=[]):
    if request.method=='POST':
        if 'search_term' in request.form:
            #getting the search result
            search_term=request.form['search_term']
            queue=search_vids(search_term)
            #creating YT object for getting title and link etc
            yt_data=id_data_creater(queue)
            print("is this stuck?")
            return render_template('search.html',title="Search",websites=websites,yt_data=yt_data,queue=queue)
        else:
            id_selected=str(request.form)[-15:-4]
            print(id_selected)
            return redirect(url_for("playlist",id_selected=id_selected))
        
    return render_template('search.html',title="Search",websites=websites)


#devices
@app.route('/devices',methods=['GET','POST'])
def device():
    return "hello"

@app.route('/playlist',methods=['GET','POST'])
def playlist():
    message=request.args['id_selected']
    return "<a href=http://youtube.com/watch?v="+message+"> play on youtube</a>"