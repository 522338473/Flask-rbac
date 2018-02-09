import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, UniqueConstraint, Index, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Menu(Base):
    """
    菜单表
    """
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))

    # 反向查询
    perm_groups = relationship('PermissonGroup', backref='perm_groups')

    def __str__(self):
        return self.title


class PermissionGroup(Base):
    """
    权限组表
    """
    __tablename__ = 'perm_group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))
    menu_id = Column(Integer, ForeignKey('menu.id'))

    permissions = relationship('Permission', backref='permissions')

    def __str__(self):
        return self.title


class Permission(Base):
    """
    权限表
    """
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))
    url = Column(String(64))
    menu_ref = Column(Integer, ForeignKey('permission.id'))
    code = Column(String(10))
    group_id = Column(Integer, ForeignKey('perm_group.id'))

    self_ref = relationship('Permission', remote_side=[id])  # 自关联

    def __str__(self):
        return self.title


class Role(Base):
    """
    角色表
    """
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10))

    def __str__(self):
        return self.name


class PermissionToRole(Base):
    """
    权限—角色关联表
    """
    __tablename__ = 'permission_role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    permission_id = Column(Integer, ForeignKey('permission.id'))
    role_id = Column(Integer, ForeignKey('role.id'))


class User(Base):
    """
    用户信息表
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(max_length=16, verbose_name='用户名')
    password = Column(max_length=16, verbose_name='密码')
    roles = ManyToManyField(to='Role', verbose_name='担任的角色', null=True, blank=True)

    def __str__(self):
        return self.username


class UserToRole(Base):
    """
    用户—角色关联表
    """
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    role_id = Column(Integer, ForeignKey('role.id'))
