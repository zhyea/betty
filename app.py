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
    from blueprints.links import links
    app.register_blueprint(links)


if __name__ == '__main__':
    app.config.from_object('tools.config.DevelopmentConfig')
    db = Database(app.config[''])
    register_bps()
    app.run(host='0.0.0.0')
