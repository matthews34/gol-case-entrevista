import os

from flask import Flask

from case_gol import database


def create_app() -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'go-case.sqlite'),
    )
    app.config.from_pyfile("config.py", silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # TODO: switch by the actual index
    @app.route('/')
    def hello() -> str:
        return 'Hello, World!'

    # initialize db
    database.init_app(app)

    # register blueprints
    from . import auth
    app.register_blueprint(auth.bp)

    return app
