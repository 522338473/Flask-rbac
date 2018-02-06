"""
测试rbac
"""

from flask import request, session, redirect, url_for, render_template

from . import rbac


@rbac.route('/test', methods=['GET'])
def test():
    # print(request)
    return '测试页面'
