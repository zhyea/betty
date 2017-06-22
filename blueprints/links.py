from flask import Blueprint, render_template

links = Blueprint('links', __name__, url_prefix='/links')


@links.route('/show', methods=['GET'])
def show_links():

    return render_template('links/show_links.html')
