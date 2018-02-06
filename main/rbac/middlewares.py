"""
自定义中间件
"""


class RbacMiddleware(object):
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        print('初始化app')

        pass

    def check_login(self):
        print('检查是否登录')

        pass
