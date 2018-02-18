from flask import Flask

from . import rbac
from .rbac.auth import Auth


def create_app():
    app = Flask(__name__)  # type:Flask

    # app.config.from_object('settings.TestConfig')
    # app.config.from_object('settings.DevConfig')
    app.config.from_object('settings.ProConfig')

    app.register_blueprint(rbac.rbac)
    Auth(app)  # 使用自定义插件添加一些功能

    return app
