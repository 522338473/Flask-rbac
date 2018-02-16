"""
自定义插件，主要功能有：
    1、添加中间件
    2、为模板添加可直接使用的变量
    3、为app提供链接到该功能内部的接口，使用current_app.auth_manager调用
"""
import re

from flask import request, session, redirect, url_for


class Auth(object):
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.auth_manager = self
        app.before_request(self.check_login)
        # app.context_processor(self.auth_context_processor)

    def auth_context_processor(self):
        """
        为模板添加可直接引用的变量
        :return: 返回一个字典，固定格式
        """
        current_user = session.get('user')
        return dict(current_user=current_user)

    def check_valid_urls(self):
        """
        验证当前url是否在白名单中
        :return:匹配到白名单中的url，返回True
        """
        current_url = request.path

        for url in self.app.config.get('VALID_URLS'):
            re_url = '^{}$'.format(url)
            if re.match(re_url, current_url):
                return True

    def check_login(self):
        """
        检测是否有用户登录，如果没有，跳转到登录页面
        """
        if self.check_valid_urls():
            return None
        if not session.get('userinfo'):
            return redirect(url_for('rbac.login'))
