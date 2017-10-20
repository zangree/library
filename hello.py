# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager

# 1.程序初始化
app = Flask(__name__)
manager = Manager(app)

# 2.写路由 视图函数
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

# 3.启动服务器
if __name__ == '__main__':
    manager.run()