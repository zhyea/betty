from flask import Blueprint

view = Blueprint("view", __name__)


@view.route('/', methods=['GET'])
def index():
    return 'Hi Betty!!'
