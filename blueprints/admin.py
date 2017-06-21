from flask import Blueprint, render_template, current_app

admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['POST'])
def login():
    return 'login'


@admin.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')


@admin.route('/logout', methods=['GET'])
def logout():
    return 'logout'
