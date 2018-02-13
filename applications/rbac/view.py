"""
测试rbac
"""

from flask import request, session, redirect, url_for, render_template, current_app

from . import rbac
from .models import User, sess


@rbac.route('/')
def test():
    new_user = User(username='mark', password='abc123')
    sess.add(new_user)
    sess.commit()
    return '测试页面'


@rbac.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if '用户名密码正确':
            return redirect(url_for('rbac.test'))
        else:
            return '登录失败'
