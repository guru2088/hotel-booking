from flask import Flask

from flask_restx.apidoc import apidoc


ROOT_URL = '/main'


def create_app(config_name):
    from main.config import app_config

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["APPLICATION_ROOT"] = ROOT_URL

    app.register_blueprint(apidoc, url_prefix=ROOT_URL)

    with app.app_context():
        from main.api_v1 import blueprint as api
        from main.healthcheck import healthcheck

        app.register_blueprint(api, url_prefix=ROOT_URL + '/api/')
        app.register_blueprint(healthcheck, url_prefix=ROOT_URL + '/version')
    return app
