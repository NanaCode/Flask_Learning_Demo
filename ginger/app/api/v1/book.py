# _*_ coding: utf-8 _*_
from flask import Blueprint

from app.libs.redprint import RedPrint

__author__ = 'Nana'
__date__ = '2018/6/17 17:01'

# blueprint
# book = Blueprint('book', __name__)


# @book.route('/v1/book/get')
# def get_book():
#     return 'get book'
#
#
# @book.route('/v1/book/create')
# def create_book():
#     return 'create book'

api = RedPrint('book')

# @api.route('/v1/book/get')
@api.route('/get')
def get_book():
    return 'get book'


# @api.route('/v1/book/create')
@api.route('/create')
def create_book():
    return 'create book'
