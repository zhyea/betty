from flask import Blueprint, render_template

from tools.database import db

user = Blueprint("user", __name__, url_prefix='/user')


@user.route('/show', methods=['GET'])
def show_users():
    users = db.find_all("select * from user order by id desc")
    print users
    return render_template('user/show_users.html', users=users)
