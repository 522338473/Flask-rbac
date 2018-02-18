from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms import validators, Form
from wtforms import widgets, StringField, PasswordField

from . import models
from .database import db_sess

LoginForm = model_form(models.User, base_class=FlaskForm, db_session=db_sess, only=['username', 'password'],
                       field_args={
                           "username": {
                               "label": '用户名',
                               "validators": [
                                   validators.DataRequired(message='用户名不能为空'),
                                   validators.Length(min=4, max=16, message='密码长度必须大于%(min)d且小于%(max)d')
                               ],
                               "render_kw": {'class': 'form-control'}
                           },
                           "password": {
                               "label": '密码',
                               "widget": widgets.PasswordInput(),
                               "validators": [
                                   validators.DataRequired(message='密码不能为空'),
                                   validators.Length(min=6, max=16, message='密码长度必须大于%(min)d且小于%(max)d')
                               ],
                               "render_kw": {'class': 'form-control'}

                           }
                       })
