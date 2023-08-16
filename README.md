# YT-remote-control

A simple python website to cast any youtube video on the chromecast on the same network

___

## Installation

The website uses flask as its backend and html/Bootstrap as its frontend.
you have to have python installed to install the application.
to install all the dependency, you can go to the directory where the program is stored and run this command

`pip install -r requirements.txt`

the website can also be used as a webapp due to the pywebview package. You do need some aditional configuration to achieve so

For any requirement problems, you can visit [This website](https://pywebview.flowrl.com/guide/installation.html#dependencies) or can open the issue on github for further assistance.

___

## Running

The program runs using the command 

`control-box --type "specify your type"`

the `--type` argument will accept 2 values `web` and `app`

The web argument will only launch the website on the port 4392, which you can access from the web browser

the app argument will just launch a applcation using webview and will exit on closing the website

___

## Further instructions are written on the app