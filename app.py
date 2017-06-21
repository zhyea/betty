from flask import Flask


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
    app.config.from_pyfile('app.cfg')
    register_bps()
    app.run(host='0.0.0.0')
