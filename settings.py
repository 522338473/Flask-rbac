# 数据库的相关配置，自行添加格式如下的信息：sql_info = ['user','password','ip','port','数据库名']
from applications.mysql_config import sql_info


class BaseConfig(object):
    """
    通用配置
    """

    SECRET_KEY = 'sls(a61ko4saf~!=dljus'
    # SECRET_KEY = os.urandom(24)  # 服务器每次重启，所有session失效，更安全
    SESSION_REFRESH_EACH_REQUEST = True


class TestConfig(BaseConfig):
    """
    测试环境配置
    """
    Test = True


class DevConfig(BaseConfig):
    """
    开发环境配置
    """
    DEV = True


class ProConfig(BaseConfig):
    """
    正式环境配置
    """

    # 数据库相关
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(*sql_info)
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 记录对象的修改

    # 权限校验白名单
    VALID_URLS = [
        '/favicon.ico',
        '/static/.*',
        '/login.*',
        '/logout',
        '/',
        '/test',
    ]

    USER_INFO = 'userinfo'
    PERM_INFO_DICT = 'perm_info_dict'
    PERM_SIDE_LIST = 'perm_side_list'
    PERM_CODES_LIST = 'perm_codes_list'
