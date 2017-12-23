#!/usr/bin/env/ python3
#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import json
from datetime import datetime


app = Flask(__name__)
app.config['TMEPLATES_AUTO_RELOAD']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name=name
    
    def __repr__(self):
        return '<Category %r>' %self.category

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content=db.Column(db.Text)
    
    def __init__(self,title,time,category,content):
        self.title=title
        self.created_time=time
        if category=='java':
            self.category_id=1
        elif category=='python':
            self.category_id=2
        self.content=content

    def __repr__(self):
        return '<File %r>'%self.title

@app.route('/')
def index():
    file_dict1={}
    file_title=[]
    #file_list=os.listdir('/home/shiyanlou/files')
    file_title=File.query.all()
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
        
