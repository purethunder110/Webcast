from pytube import Search,YouTube
from datetime import timedelta
#for chromecast functionality
import pychromecast


def search_vids(search_term):
    search_obj=Search(search_term)
    result_list=list(search_obj.results)
    j=0
    stack=[]
    for i in result_list:
        stack.insert(j,str(i)[-12:-1])
        j+=1
    
    return stack


def id_data_creater(id_list):
    yt_obj_dic=dict()
    for i in id_list:
        yt_obj=YouTube('http://youtube.com/watch?v='+i)
        yt_obj_dic[i]=[yt_obj.thumbnail_url,yt_obj.title,str(timedelta(seconds=yt_obj.length)),yt_obj.channel_url,yt_obj.author]
    return yt_obj_dic


def device_connection_establishment():
    services,browser=pychromecast.discovery.discover_chromecasts()
    k=0
    device_name=dict()
    for i in services:
        device_name[k]=[str(i.friendly_name),str(i.model_name),str(i.uuid),str(i.host)]
        k+=1
    return device_name