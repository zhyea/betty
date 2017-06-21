from flask import Blueprint, render_template, current_app, request

from tools.database import Database

admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = Database(current_app.config['DB_CONFIG'])
    result = db.query("SELECT * FROM user WHERE username=%s AND password =%s", username, password)
    if result is not None:
        return 'login'
    else:
        error = 'Invalid username or password!'
    return render_template('login.html', error=error)


@admin.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')


@admin.route('/logout', methods=['GET'])
def logout():
    return 'logout'
