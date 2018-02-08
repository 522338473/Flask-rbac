"""
自定义用户认证功能
"""

from flask import request, session


class RbacMiddleware(object):
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        # print('为app添加用户认证功能')
        app.auth_manager = self

        pass

    def check_login(self, request):
        """
        模拟关于用户认证的一些操作，这里只是简单写一个功能
        """
        # 这里应该从数据库中获取数据，进行用户名和密码的校验
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'mark' and password == 'abc123':
            return True
        return False
