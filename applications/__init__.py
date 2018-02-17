from flask import Flask, request, session, redirect, url_for
from werkzeug.routing import BaseConverter


def create_app():
    app = Flask(__name__)  # type:Flask
    app.debug = True

    # app.config.from_object('settings.TestConfig')
    # app.config.from_object('settings.DevConfig')
    app.config.from_object('settings.ProConfig')

    # print(app.config)



    return app
