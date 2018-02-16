class BaseConfig(object):
    SECRET_KEY = 'sls(al1xx4saf~!=dljus'
    SESSION_REFRESH_EACH_REQUEST = True


class TestConfig(BaseConfig):
    """
    测试配置
    """
    Test = True


class DevConfig(BaseConfig):
    """
    开发配置
    """
    DEV = True


class ProConfig(BaseConfig):
    """
    正式配置
    """
    VALID_URLS = [
        '/favicon.ico',
        '/static/.*',
        '/login.*',
        '/logout',
    ]
