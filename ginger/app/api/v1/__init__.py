# _*_ coding: utf-8 _*_
from flask import Blueprint
# from app.api.v1.book import api as book
# from app.api.v1.user import api as user
from app.api.v1 import user, book, client

__author__ = 'Nana'
__date__ = '2018/6/17 16:59'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    # user.api.register(bp_v1, url_prefix='/user')
    # book.api.register(bp_v1, url_prefix='/book')
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1
