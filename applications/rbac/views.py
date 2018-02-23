"""
测试rbac
"""
from flask import request, session, current_app
from flask import redirect, url_for, render_template

from applications import db
from . import rbac  # 蓝图
from . import models, forms
from .service import init_permission


class Codes(object):
    """
    封装session中权限的codes信息，便于在模板中调用
    """

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
    """
    主页
    """
    userinfo = session.get(current_app.config["USER_INFO"])
    if userinfo:
        urls_info = session.get(current_app.config["PERM_SIDE_LIST"])
        return render_template('index.html', urls_info=urls_info)
    else:
        return render_template('index.html')


@rbac.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录
    """
    if request.method == 'GET':
        login_form = forms.UserForm()
        return render_template('login.html', login_form=login_form)
    else:
        login_form = forms.LoginForm(request.form)
        if not login_form.validate_on_submit():
            return render_template('login.html', login_form=login_form)
        else:
            username = login_form.data.get('username')
            password = login_form.data.get('password')

            user_obj = db.session.query(models.User).filter_by(username=username).first()

            if user_obj:
                if user_obj.check_password(password):
                    init_permission(user_obj)
                    return redirect(url_for('rbac.index'))
                else:
                    login_form.password.errors.append('密码错误')
                    return render_template('login.html', login_form=login_form)
            else:
                login_form.username.errors.append('用户不存在')
                return render_template('login.html', login_form=login_form)


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
    # from werkzeug.security import generate_password_hash
    # new_user = models.User(username='test', password=generate_password_hash('abc123'))
    # db.session.add(new_user)
    # db.session.commit()

    # 修改密码
    # objs = db.session.query(models.User).all()
    # for obj in objs:
    #     obj.password = generate_password_hash('abc123')
    # db.session.commit()

    return '测试'


###### 用户相关 ######
@rbac.route('/userinfo')
def userinfo():
    codes = Codes(session.get(current_app.config["PERM_CODES_LIST"]))
    user_list = db.session.query(models.User).all()
    res = render_template('userinfo.html', codes=codes, user_list=user_list)
    return res


@rbac.route('/userinfo/add', methods=['GET', 'POST'])
def user_add():
    if request.method == 'GET':
        user_form = forms.LoginForm()
        return render_template('user_add.html', user_form=user_form)
    else:
        user_form = forms.LoginForm(request.form)
        if not user_form.validate_on_submit():
            return render_template('user_add.html', user_form=user_form)
        else:
            username = user_form.data.get('username')
            password = user_form.data.get('password')
            new_user = models.User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()

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
    # db.session.query(models.User).filter_by(id=id).delete()
    # db.session.commit()
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
