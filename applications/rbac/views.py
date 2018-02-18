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

# 数据库的相关配置，自行添加格式如下的信息：sql_info = ['user','password','ip','port','数据库名']
from applications.mysql_config import sql_info


class Codes(object):
    def __init__(self, codes_list):
        self.codes_list = codes_list

    def has_add(self):
        if 'add' in self.codes_list:
            return True

    def has_edit(self):
        if 'edit' in self.codes_list:
            return True

    def has_del(self):
        if 'del' in self.codes_list:
            return True


@rbac.route('/')
def index():
    userinfo = session.get('userinfo')
    if userinfo:
        urls_info = session.get('PERM_SIDE_LIST')
        return render_template('index.html', urls_info=urls_info)
    else:
        return render_template('index.html')


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

            engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(*sql_info))
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


@rbac.route('/test')
def test():
    # 创建用户
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(*sql_info))
    DBSession = sessionmaker(bind=engine)
    db_sess = DBSession()

    new_user = models.User(username='test', password='abc123')
    db_sess.add(new_user)
    db_sess.commit()

    db_sess.close()

    return '测试'


###### 用户相关 ######
@rbac.route('/userinfo')
def userinfo():
    codes = Codes(session.get('PERM_CODES_LIST'))

    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(*sql_info))
    DBSession = sessionmaker(bind=engine)
    db_sess = DBSession()

    user_list = db_sess.query(models.User).all()

    res = render_template('userinfo.html', codes=codes, user_list=user_list)
    db_sess.close()
    return res


@rbac.route('/userinfo/add', methods=['GET', 'POST'])
def user_add():
    return '添加用户或注册'


@rbac.route('/userinfo/edit/<int:id>', methods=['GET', 'POST'])
def user_edit(id):
    if request.method == 'GET':
        # 此处仅为测试，具体业务逻辑请自行实现
        return '编辑用户'
    else:
        # 此处仅为测试，具体业务逻辑请自行实现
        return 'POST提交编辑用户'


@rbac.route('/userinfo/del/<int:id>')
def user_del(id):
    # engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(*sql_info))
    # DBSession = sessionmaker(bind=engine)
    # db_sess = DBSession()
    #
    # db_sess.query(models.User).filter_by(id=id).delete()
    #
    # db_sess.commit()
    # db_sess.close()
    # return redirect(url_for('rbac.userinfo'))

    return '删除用户'


###### 订单相关 ######
@rbac.route('/order')
def order():
    return render_template('order.html')


@rbac.route('/order/add', methods=['GET', 'POST'])
def order_add():
    return '添加用户或注册'


@rbac.route('/order/edit/<int:id>', methods=['GET', 'POST'])
def order_edit(id):
    if request.method == 'GET':
        # 此处仅为测试，具体业务逻辑请自行实现
        return '编辑订单'
    else:
        # 此处仅为测试，具体业务逻辑请自行实现
        return 'POST提交编辑订单'


@rbac.route('/order/del/<int:id>')
def order_del(id):
    return '删除订单'
