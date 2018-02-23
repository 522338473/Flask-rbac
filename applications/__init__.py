from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)  # type:Flask
    app.debug = True

    # app.config.from_object('settings.TestConfig')
    # app.config.from_object('settings.DevConfig')
    app.config.from_object('settings.ProConfig')
    db.init_app(app)  # 在app.config中添加db相关的配置

    from . import rbac
    from .rbac.auth import Auth
    app.register_blueprint(rbac.rbac)
    Auth(app)  # 使用自定义插件添加一些功能

    return app
