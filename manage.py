from flask_script import Manager, Server

from applications import create_app

app = create_app()

from applications.rbac.plugins import Auth
from applications import rbac

app.register_blueprint(rbac.rbac)

Auth(app)  # 使用自定义插件添加一些功能

# manager = Manager(app)  # type:Manager
# manager.add_command("runserver", Server())

if __name__ == '__main__':
    # print(app.url_map)
    # print(app.url_map._rules)
    # print(app.config.root_path)
    # print(app.config)
    # manager.run()

    app.run()
