from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms import validators
from wtforms import widgets

from applications import db
from . import models

LoginForm = model_form(models.User, base_class=FlaskForm, db_session=db.session, only=['username', 'password'],
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

UserForm = model_form(models.User, base_class=FlaskForm, db_session=db.session, exclude=['create_time'],
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

                          },
                          "roles": {
                              "label": '角色',
                              "widget": widgets.Select(),
                              "validators": [
                                  validators.DataRequired(message='角色不能为空'),
                              ],
                              "render_kw": {'class': 'form-control'}
                          }
                      })
