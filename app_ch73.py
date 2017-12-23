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
        if category.name=='Java':
            self.category_id=1
        elif category.name=='Python':
            self.category_id=2
        self.content=content

    def __repr__(self):
        return self.title,self.id

@app.route('/')
def index():
    file_title,file_id=File.query.all()
    #file_list=db.engine.execute('select * from file').fetchall()

    return render_template('index.html',title=file_title,id=file_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


@app.route('/files/<file_id>')
def file(file_id):
    file_list=db.engine.execute('select * from file where id='+file_id).fetchall()
    if len(file_list)>0:
        if file_list[0][3]==1:
            file_category='Java'
        else:
            file_category='Python'
        return render_template('file.html',content=file_list,category=file_category)
    else:
        return not_found(404)
        
