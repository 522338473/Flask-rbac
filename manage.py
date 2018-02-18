from flask_script import Manager, Server
from applications import create_app

app = create_app()

# manager = Manager(app)  # type:Manager
# manager.add_command("runserver", Server())

if __name__ == '__main__':
    # print(app.url_map)
    # print(app.url_map._rules)
    # print(app.config.root_path)
    # print(app.config)

    # manager.run()
    app.run(debug=True)
