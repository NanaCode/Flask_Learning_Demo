# _*_ coding: utf-8 _*_
from wtforms import ValidationError
from wtforms.validators import DataRequired, length, Regexp, Email

from app.libs.enums import ClientTypeEnum
from app.models.user import User

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
        self.type.data = client


# 解决form没有nickname参数的问题
class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters, numbers and '_'
        Regexp(r'^[A-Za-z0-9_*$#@]{6, 22}$')  # 密码长度6-22位
    ])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    # 验证账号是否已经注册过
    # 面向对象的继承特性来减少代码的编写量
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
