from flask import Blueprint, render_template

link = Blueprint('link', __name__, url_prefix='/links')


@link.route('/show', methods=['GET'])
def show_links():

    return render_template('links/show_users.html')
