#!/usr/bin/env/ python3
#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import json
from datetime import datetime
from pymongo import MongoClient


app = Flask(__name__)
app.config['TMEPLATES_AUTO_RELOAD']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)
client=MongoClient('127.0.0.1',27017)
mongo_db=client.shiyanlou

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files=db.relationship('File',backref=db.backref('category',lazy='select'))

    def __init__(self,name):
        __tablename__='category'
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
        __tablename__='file'
        self.title=title
        self.created_time=time
        self.category_id=category.id
        self.content=content

    def add_tag(self, tag_name):
        self.name=tag_name
        tag_file=self.title
        find_list=list(mongo_db.tag.find({'name':self.name,'file_id':tag_file}))
        if not bool(find_list):
            mongo_db.tag.insert_one({'name':self.name,'file_id':tag_file})
        else:
            print('Tag already exists!')

    def remove_tag(self,tag_name):
        self.name=tag_name
        tag_file=self.title
        mongo_db.tag.delete_one({'name':self.name,'file_id':tag_file})

    @property
    def tags(self):
        return  list(mongo_db.tag.find({'file_id':self.title},{'file_id':0,'_id':0}))


@app.route('/')
def index():
    files_result=File.query.all()
    return render_template('index.html',files=files_result)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


@app.route('/files/<file_id>')
def file(file_id):
    file_list=db.engine.execute('select * from file where id='+file_id).fetchall()
    if len(file_list)>0:
        cateID=str(file_list[0][3])
        file_category=db.engine.execute('select * from category where id='+cateID).fetchall()
        return render_template('file.html',content=file_list,category=file_category[0][1])
    else:
        return not_found(404)
        
