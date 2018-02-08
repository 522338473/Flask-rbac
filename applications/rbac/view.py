"""
测试rbac
"""

from flask import request, session, redirect, url_for, render_template, current_app
from .middlewares import RbacMiddleware
from . import rbac


@rbac.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        auth_manager = current_app.auth_manager  # type:RbacMiddleware
        if auth_manager.check_login(request):
            return '登录成功'
        else:
            return '登录失败'
