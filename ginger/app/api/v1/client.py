# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/17 21:20'

from app.libs.redprint import RedPrint

api = RedPrint('client')


@api.route('/register')
def create_client():
    """
    用户客户端注册 登录
    参数 校验 接收参数
    WTForms 参数校验 验证表单
    :return:
    """
    pass
