import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Table

# 数据库的相关配置，自行添加格式如下的信息：sql_info = ['user','password','ip','port','数据库名']
from applications.mysql_config import sql_info

Base = declarative_base()


class Menu(Base):
    """
    菜单表
    """
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))

    # 双向关联，用于跨表查询
    perm_groups = relationship('PermissionGroup', backref='menu')

    def __str__(self):
        return self.title


class PermissionGroup(Base):
    """
    权限组表
    """
    __tablename__ = 'permissiongroup'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))
    menu_id = Column(Integer, ForeignKey('menu.id'))

    # 双向关联，用于跨表查询
    permissions = relationship('Permission', backref='perm_group')

    def __str__(self):
        return self.title


# 权限—角色关联表
permission_role = Table('permission_role', Base.metadata,
                        Column('permission_id', Integer, ForeignKey('permission.id')),
                        Column('role_id', Integer, ForeignKey('role.id')))


class Permission(Base):
    """
    权限表
    """
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))
    url = Column(String(64))
    menu_ref = Column(Integer, ForeignKey('permission.id'))  # 自关联
    code = Column(String(10))
    group_id = Column(Integer, ForeignKey('permissiongroup.id'))

    # 自关联声明
    self_ref = relationship('Permission', remote_side=[id])

    # 多对多的双向关联，用于跨表查询
    roles = relationship('Role', secondary=permission_role, backref='permissions')

    def __str__(self):
        return self.title


# 用户—角色关联表
user_role = Table('user_role', Base.metadata,
                  Column('user_id', Integer, ForeignKey('user.id')),
                  Column('role_id', Integer, ForeignKey('role.id')))


class Role(Base):
    """
    角色表
    """
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10))

    # 双向关联，用于跨表查询
    users = relationship('User', secondary=user_role, backref='roles')

    def __str__(self):
        return self.name


class User(Base):
    """
    用户信息表
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16))
    password = Column(String(16))
    create_time = Column(DateTime, default=datetime.datetime.now)

    def __str__(self):
        return self.username

# engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(*sql_info))

# 在数据库中创建表
# Base.metadata.create_all(engine)
# 在数据库中删除表
# Base.metadata.drop_all(engine)


# 笔记：
# 一对一关联的时候，在relationship里设置uselist为False
# 在Association-object模式中，级联删除要设置viewonly为False，待研究
