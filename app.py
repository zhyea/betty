from flask import Flask

from tools.database import Database

app = Flask(__name__)


def register_bps():
    from blueprints.admin import admin
    app.register_blueprint(admin)
    from blueprints.view import view
    app.register_blueprint(view)
    from blueprints.user import user
    app.register_blueprint(user)
    from blueprints.category import cat
    app.register_blueprint(cat)
    from blueprints.link import link
    app.register_blueprint(link)


def init():
    Database().init(app.config['DB_CONFIG'])
    register_bps()


if __name__ == '__main__':
    app.config.from_object('tools.config.DevelopmentConfig')
    init()
    app.run(host='0.0.0.0')
