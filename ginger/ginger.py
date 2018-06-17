# _*_ coding: utf-8 _*_
from app.app import create_app

__author__ = 'Nana'
__date__ = '2018/6/17 16:37'

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # 启动web服务器 打开调试模式
