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


# REST
REST 把服务器所有数据视作资源

1. 使用URI来定位资源
2. 使用HTTP动词操作资源  GET  POST PUT DELETE
localhost:5000/v1/user 定位user这个资源， 定位到资源才能进行资源的操作
操作数据库 增删改查 
localhost:5000/v1/user/get 这种写法不符合REST规范 URI只能定位资源，不能表达如何操作资源
视图函数的URI根本就不应该包含动词

REST要求一定要携带版本号
版本号加在URI中只是众多方案中的一种，很多设计把版本号加在HTTP的头里
版本号加在URI问号后面，用查询参数的方式传递到服务器中

# REST不适合内部开发
理论是理论，实践是实践
真实开发，不会严格照搬REST
REST不是适合所有的场景
API场景分类：内部开发API 开放API
标准REST API适合用在开放API
开放API不会考虑具体前端是什么 豆瓣 微博 github

资源 CRUD
user_standard_rest.py  增删改查操作

REST 接口粒度比较粗 前端开发起来不方便

REST造成HTTP请求数量大幅增加

REST把一切看作资源 不太考虑业务逻辑

REST适合做开放型API  只提供数据 不管业务逻辑

REST很好的标准和规范：
1. 强制要求接口返回JSON
2. 强制要求要带版本号 等等

遵守REST 灵活

让接口具有业务处理的性质

后台 js必须学










