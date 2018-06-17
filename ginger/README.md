Python3.6
Flask1.0
MySQL

Flask Changelog 1.0
http://flask.pocoo.org/docs/1.0/changelog/#version-1-0

# 初始化项目
## 创建虚拟环境
### 项目目录下： pipenv install

## 激活虚拟环境
### pipenv shell

## 项目依赖
### pipenv graph

## 查看虚拟环境名字和路径
### pipenv --venv
#### C:\Users\Administrator\Envs\ginger-Rx32UybM


Pipfile 记录项目所有相关包

新建入口文件： 文字名字通常和项目同名

不推荐在实例化Flask核心对象

Alt Enter： Python自动导入包

实例化Flask核心对象以后，需要把整个项目的配置文件导入到Flask核心对象中

secure.py API敏感配置项
settings.py 通用配置选项

v1 版本号的作用

视图函数模块中导入app, 做法不可取，可能会导致循环导入
可以使用蓝图blueprint来注册路由

Flask设计视图函数不是用来拆分视图函数的
蓝图应该是模块级别的拆分，而不是视图函数级别的拆分

构建自定义对象 红图 redprint

libs 存放自定义模块

创建v1蓝图

@api.route('/v1/book/create')
v1放到蓝图上，book放到红图上

编写类，首先需要考虑构造函数

实现route装饰器

endpoint概念很重要

学习  学的是思路，而不是标准答案







