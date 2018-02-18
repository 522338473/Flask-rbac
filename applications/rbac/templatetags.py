from flask import current_app

### 开发用，过后删除 ###
from flask import Flask

current_app = current_app  # type:Flask


######

@current_app.template_global
def xxx(m, n):
    return 1
