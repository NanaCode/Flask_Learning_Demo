# _*_ coding: utf-8 _*_
from app.libs.enums import ClientTypeEnum

__author__ = 'Nana'
__date__ = '2018/6/17 21:20'

from app.libs.redprint import RedPrint
from app.validators.forms import ClientForm

api = RedPrint('client')


@api.route('/register', method=['POST'])
def create_client():
    """
    用户客户端注册 登录
    参数 校验 接收参数
    WTForms 参数校验 验证表单
    表单和JSON对象提交过来的参数的区别： 表单-网页 json-移动端
    客户端提交数据的方式有很多种
    :return:
    """
    # request.json
    # request.args.to_dict()
    data = request.json
    form = ClientForm(data=data)  # 注意，json形式需要data=data
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
    pass


def __register_user_by_email():
    pass
