"""
测试rbac
"""

from flask import request, session, redirect, url_for, render_template, current_app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
from sqlalchemy import and_, or_

from flask_sqlalchemy import SQLAlchemy

from . import rbac  # 蓝图
from . import models
from . import forms
from .service import init_permission


@rbac.route('/')
def index():
    userinfo = session.get('userinfo')
    if userinfo:
        urls_info = session.get('PERM_SIDE_LIST')
        return render_template('index.html', urls_info=urls_info)
    else:
        return render_template('index.html')


@rbac.route('/test')
def test():
    # # 创建用户
    # engine = create_engine('mysql+pymysql://root:@localhost:3306/flaskrbac?charset=utf8')
    # DBSession = sessionmaker(bind=engine)
    # db_sess = DBSession()
    #
    # new_user = models.User(username='bob', password='abc123')
    # db_sess.add(new_user)
    # db_sess.commit()
    #
    # db_sess.close()

    return '测试'


@rbac.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录
    """
    if request.method == 'GET':
        login_form = forms.LoginForm()
        return render_template('login.html', login_form=login_form)
    else:
        login_form = forms.LoginForm(request.form)
        if not login_form.validate():
            return render_template('login.html', login_form=login_form)
        else:
            username = login_form.data.get('username')
            password = login_form.data.get('password')

            engine = create_engine('mysql+pymysql://root:@localhost:3306/flaskrbac?charset=utf8')
            DBSession = sessionmaker(bind=engine)
            db_sess = DBSession()

            user_obj = db_sess.query(models.User).filter(
                and_(models.User.username == username, models.User.password == password)).first()

            if not user_obj:
                return redirect(url_for('rbac.login'))
            else:
                init_permission(user_obj)
                return redirect(url_for('rbac.index'))


@rbac.route('/logout')
def logout():
    """
    注销
    """
    session.clear()
    return redirect(url_for('rbac.login'))
