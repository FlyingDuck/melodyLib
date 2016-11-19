# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    '''
    基础配置
    '''
    SECRET_KEY = '693bda65112eb4b1eab2bfe3fa8e672ad220fa7c'


class DevConfig(BaseConfig):
    '''
     开发环境配置
    '''
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass



class ProdConfig(BaseConfig):
    '''
    线上环境配置
    '''
    DEBUG = False

    @staticmethod
    def init_app(app):
        pass


config = {
    'dev': DevConfig,
    'prod': ProdConfig
}
