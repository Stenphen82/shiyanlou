from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['TMEPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    list=os.listdir('/home/shiyanlou/files')
    str2=''
    for item in list:
        str2=str2+str(item)+'\n'
    return str2

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


@app.route('/files/<filename>')
def file(filename):
    str1=str(filename)
    if os.path.exists('/home/shiyanlou/files/'+str1):
        return 'the file path is:'+str1
    else:
        return not_found(404)
        
