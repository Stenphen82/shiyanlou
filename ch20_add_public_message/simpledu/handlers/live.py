from flask import Blueprint,render_template
from simpledu.models import Live

live = Blueprint('live',__name__,url_prefix='/live')

@live.route('/')
def index():
    lives=Live.query.all()
    return render_template('live/index.html',lives=lives)

