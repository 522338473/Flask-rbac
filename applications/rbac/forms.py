from wtforms import Form

from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple

from wtforms import validators
from wtforms import widgets


class LoginForm(Form):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Length(min=4, max=16, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        render_kw={'class': 'form-control'},
    )

    password = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=6, max=16, message='密码长度必须大于%(min)d且小于%(max)d')
        ],
        render_kw={'class': 'form-control'}
    )
