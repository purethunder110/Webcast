from flask import Flask,render_template,request,redirect,url_for,make_response
from ytcast import search_vids,id_data_creater,device_connection_establishment

app=Flask(__name__)


queue=[]
websites=["About","Devices","Search"]
yt_data=dict()



#homepage
@app.route('/')
def homepage():
    queue=send_data=[]
    return render_template("about.html",title="About",websites=websites)


@app.route('/About')
def about_redirect():
    return redirect('/')


#search page
@app.route('/Search',methods=['GET','POST'])
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
            #setting cookies
            resp=make_response(redirect(url_for("Video")))
            resp.set_cookie('id_selected',str(request.form)[-15:-4])
            #id_selected=str(request.form)[-15:-4]
            #print(id_selected)
            return resp
        
    return render_template('search.html',title="Search",websites=websites)


#devices
@app.route('/Devices',methods=['GET','POST'])
def device():
    device_name=device_connection_establishment()
    return render_template("device.html",title="Device",websites=websites,device_name=device_name)

@app.route('/Video',methods=['GET','POST'])
def playlist():
    message=str(request.cookies.get('id_selected'))
    print(message)
    return render_template('video.html',title="Video",message=message)