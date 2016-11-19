# -*- coding: utf-8 -*-
from flask_script import Manager, Server


from app.factory import create_app


app = create_app('dev')
manager = Manager(app)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()
