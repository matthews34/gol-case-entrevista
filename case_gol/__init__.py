import os

from flask import Flask

from case_gol import database
from case_gol.config import config_manager


def create_app() -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(DATABASE=os.path.join(app.instance_path, "go-case.sqlite"))
    app.config.from_object(config_manager[os.getenv("APP_ENVIRONMENT", "dev")])

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize db
    database.init_app(app)

    # register blueprints
    from . import auth

    app.register_blueprint(auth.bp)

    from . import stats

    app.register_blueprint(stats.bp)
    app.add_url_rule("/", endpoint="index")

    return app
