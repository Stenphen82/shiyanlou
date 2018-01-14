from flask import Blueprint, render_template
from simpledu.models import db, User, Course
user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    query_user=User.query.filter_by(username=username).first()
    if bool(query_user):
        courses=Course.query.filter_by(author_id=query_user.id)
        return render_template('user.html', user=query_user,courses=courses)
    else:
        return not_found(404)


@user.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404



