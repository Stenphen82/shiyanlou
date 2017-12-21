#!/usr/bin/env/ python3
#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)
app.config['TMEPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    file_dict1={}
    file_title=[]
    file_list=os.listdir('/home/shiyanlou/files')
    for item in file_list:
        file_path='/home/shiyanlou/files/'+item
        with open(file_path,'r') as open_file:
            file_dict1=json.loads(open_file.read())
            file_title.append(file_dict1["title"])
    return render_template('index.html',title=file_title)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


@app.route('/files/<filename>')
def file(filename):
    file_dict2={}
    if os.path.exists('/home/shiyanlou/files/'+filename+'.json'):
        file_path='/home/shiyanlou/files/'+filename+'.json'
        with open(file_path,'r') as open_file:
            file_dict2=json.loads(open_file.read())
            return render_template('file.html',content=file_dict2['content'])
    else:
        return not_found(404)
        
