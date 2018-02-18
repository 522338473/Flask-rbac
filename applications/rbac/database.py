from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 数据库的相关配置，自行添加格式如下的信息：sql_info = ['user','password','ip','port','数据库名']
from applications.mysql_config import sql_info

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(*sql_info))
DBSession = sessionmaker(bind=engine)
db_sess = DBSession()
