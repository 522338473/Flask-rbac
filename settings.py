class BaseConfig(object):
    """
    通用配置
    """
    SECRET_KEY = 'sls(al1xx4saf~!=dljus'
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
    VALID_URLS = [
        '/favicon.ico',
        '/static/.*',
        '/login.*',
        '/logout',
        '/',
        '/test',
    ]

    # PERM_INFO_DICT = 'perm_info_dict'
    # PERM_SIDE_LIST = 'perm_side_list'
