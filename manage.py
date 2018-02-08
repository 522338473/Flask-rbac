from flask_script import Manager, Server

from applications import create_app
from applications.rbac.middlewares import RbacMiddleware

app = create_app()
RbacMiddleware(app)  # 为原app添加中间件

# manager = Manager(app)  # type:Manager
# manager.add_command("runserver", Server())

if __name__ == '__main__':
    # print(app.url_map)
    # print(app.url_map._rules)
    # print(app.config.root_path)
    # print(app.config)
    # manager.run()

    app.run()
