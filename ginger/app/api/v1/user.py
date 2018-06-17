# _*_ coding: utf-8 _*_
from flask import Blueprint

from app.libs.redprint import RedPrint

__author__ = 'Nana'
__date__ = '2018/6/17 17:01'

# user = Blueprint('user', __name__)

# @user.route('/v1/user/get')
# def get_user():
#     return 'I am Nana!'

api = RedPrint('user')


# @api.route('/v1/user/get')
@api.route('/get')
def get_user():
    return 'I am Nana!'
