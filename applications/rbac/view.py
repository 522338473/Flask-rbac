"""
测试rbac
"""

from flask import request, session, redirect, url_for, render_template, current_app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text

from flask_sqlalchemy import SQLAlchemy

from . import rbac
from . import models


@rbac.route('/')
def test():
    engine = create_engine('mysql+pymysql://root:@localhost:3306/flaskrbac?charset=utf8')
    DBSession = sessionmaker(bind=engine)
    db_sess = DBSession()

    # new_user = models.User(username='mark', password='abc123')
    # db_sess.add(new_user)
    # db_sess.commit()

    db_sess.close()

    return '测试页面'


@rbac.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if '用户名密码正确':
            session['user'] = 'mark'
            return redirect(url_for('rbac.test'))
        else:
            return '登录失败'


@rbac.route('/logout')
def logout():
    session.clear()
    return
