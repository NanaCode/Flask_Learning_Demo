# _*_ coding: utf-8 _*_
from enum import Enum

__author__ = 'Nana'
__date__ = '2018/6/17 21:25'


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201

