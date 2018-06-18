# _*_ coding: utf-8 _*_
from sqlalchemy import Integer, Column, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db

__author__ = 'Nana'
__date__ = '2018/6/18 9:08'


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)  # 权限标识 1-普通用户 2-管理员
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)