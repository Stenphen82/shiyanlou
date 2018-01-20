from flask import Blueprint, render_template
from .ws import redis

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    return render_template('live/index.html')

@live.route('/systemmessage')
def send_message(message):
    redis.publish('chat',message)
    return render_template('admin/index.html')


