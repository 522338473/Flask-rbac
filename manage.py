from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from applications import db, create_app

app = create_app()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    # print(app.url_map)
    # print(app.url_map._rules)
    # print(app.config.root_path)
    # print(app.config)

    # manager.run()
    app.run()
