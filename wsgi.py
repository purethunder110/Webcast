from flask import Flask,render_template,request,redirect,url_for,make_response
from ytcast import search_vids,id_data_creater,device_detection,cast_video

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

#devices
@app.route('/Devices',methods=['GET','POST'])
def device():
    device_name=device_detection()
    if request.method=='POST':
        resp=make_response(redirect('Search'))
        name_of_device=request.form["name_of_device"]
        resp.set_cookie('name_of_device',str(name_of_device))
        return resp
    return render_template("device.html",title="Device",websites=websites,device_name=device_name)


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
            return render_template('search.html',title="Search",websites=websites,yt_data=yt_data,queue=queue)
        else:
            #setting cookies
            resp=make_response(redirect(url_for("Video")))
            resp.set_cookie('id_selected',str(request.form['video_id']))

            return resp
        
    return render_template('search.html',title="Search",websites=websites)



@app.route('/Video',methods=['GET','POST'])
def Video():
    message=request.cookies.get('id_selected')
    name_of_device=request.cookies.get('name_of_device')
    cast_video(name_of_device,message)
    #return render_template('video.html',message=message)
    resp=make_response(redirect(url_for('searchpage')))
    return resp