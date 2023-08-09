from wsgi import app
import subprocess

#subprocess.Popen("waitress-serve --host 127.0.0.1 --call wsgi:app",shell=True)

app.run(debug=True)