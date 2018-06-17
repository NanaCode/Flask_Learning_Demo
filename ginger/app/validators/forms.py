# _*_ coding: utf-8 _*_
from wtforms.validators import DataRequired, length

from app.libs.enums import ClientTypeEnum

__author__ = 'Nana'
__date__ = '2018/6/17 21:28'

from wtforms import Form, StringField, IntegerField


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()  # 有些客户端不需要传入密码
    type = IntegerField(validators=[DataRequired])  # 客户端类型

    # 枚举的可读性比数字强
    # 承接类型转换，实现数字向枚举的转换
    # 項目中最好不要使用数字代表枚举类型，而应该使用枚举来代表不同的类型
    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value)
        except ValueError as e:
            raise e
