# _*_ coding: utf-8 _*_
from flask import Flask

# from app.api.v1.user import user
# from app.api.v1.book import book
from app.api.v1 import create_blueprint_v1
from app.models.base import db

__author__ = 'Nana'
__date__ = '2018/6/17 16:39'


def register_blueprint(app):
    # app.register_blueprint(user)
    # app.register_blueprint(book)
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)  # 实例化Flask核心对象需要指定位置信息
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.settings')

    register_blueprint(app)
    register_plugin(app)

    return app
