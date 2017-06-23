from flask import Blueprint, render_template, request, session, url_for, redirect

from tools.database import db

admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    curr_user = db.find_all("SELECT * FROM user WHERE username=%s AND password =%s ORDER BY id DESC", username,
                            password)
    if curr_user is not None:
        session['is_login'] = True
        session['user'] = curr_user
        return redirect(url_for('user.show_users'))
    else:
        error = 'Invalid username or password!'
    return render_template('login.html', error=error)


@admin.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')


@admin.route('/logout', methods=['GET'])
def logout():
    return 'logout'
