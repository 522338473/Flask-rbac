from flask import Flask, request, session, redirect, url_for
from werkzeug.routing import BaseConverter


def create_app():
    app = Flask(__name__)  # type:Flask
    app.debug = True

    # app.config.from_object('settings.TestConfig')
    # app.config.from_object('settings.DevConfig')
    app.config.from_object('settings.ProConfig')

    # print(app.config)

    @app.before_request
    def auth():
        # print('中间件1')
        pass

    @app.after_request
    def after_auth(response):
        # print('中间件2')
        return response

    from applications import rbac
    app.register_blueprint(rbac.rbac)

    return app
