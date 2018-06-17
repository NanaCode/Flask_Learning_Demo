# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/17 19:50'
from app.libs.redprint import RedPrint

api = RedPrint('user')


@api.route('', methods=['GET'])
def get_user():
    return 'I am Nana!'


@api.route('', methods=['PUT'])
def update_user():
    return 'Update Nana!'


@api.route('', methods=['DELETE'])
def delete_user():
    return 'Delete Nana!'


@api.route('', methods=['POST'])
def create_user():
    return 'Create Nana!'
