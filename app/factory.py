# -*- coding: utf-8 -*-
from flask import Flask

from app.config import config


def create_app(config_name='dev'):
    app = Flask(__name__)

    # 导入配置
    current_config = config[config_name]
    app.config.from_object(current_config)
    current_config.init_app(app)

    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.melody import melody as melody_blueprint
    app.register_blueprint(melody_blueprint)

    return app

