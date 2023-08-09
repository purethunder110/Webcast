from wsgi import app
import webview
import sys
import threading
import argparse

#argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--type",required=True,help="type of function that you want to execute. web for website and app for application")

def start_server():
    app.run(host='0.0.0.0',port=5000)

if __name__ == '__main__':
    args=parser.parse_args()
    if args.type=="web":
        start_server()
    elif args.type=="app":
        t = threading.Thread(target=start_server)
        t.daemon = True
        t.start()
        webview.create_window("yt-remote-control","http://localhost:5000/",confirm_close=True,)
        webview.start()
        sys.exit()
    else:
        raise "--type argument is wrong. it could either be a 'web' type or a 'app' type"