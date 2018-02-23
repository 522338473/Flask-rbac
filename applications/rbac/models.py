import datetime

from applications import db


class Menu(db.Model):
    """
    菜单表
    """
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10))

    # 双向关联，用于跨表查询
    perm_groups = db.relationship('PermissionGroup', backref='menu')

    def __str__(self):
        return '<Menu %s>' % self.title


class PermissionGroup(db.Model):
    """
    权限组表
    """
    __tablename__ = 'permissiongroup'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))

    # 双向关联，用于跨表查询
    permissions = db.relationship('Permission', backref='perm_group')

    def __str__(self):
        return '<PermissionGroup %s>' % self.title


# 权限—角色关联表
permission_role = db.Table('permission_role', db.metadata,
                           db.Column('permission_id', db.Integer, db.ForeignKey('permission.id')),
                           db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class Permission(db.Model):
    """
    权限表
    """
    __tablename__ = 'permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10))
    url = db.Column(db.String(64))
    menu_ref = db.Column(db.Integer, db.ForeignKey('permission.id'))  # 自关联
    code = db.Column(db.String(10))
    group_id = db.Column(db.Integer, db.ForeignKey('permissiongroup.id'))

    # 自关联声明
    self_ref = db.relationship('Permission', remote_side=[id])

    # 多对多的双向关联，用于跨表查询
    roles = db.relationship('Role', secondary=permission_role, backref='permissions')

    def __str__(self):
        return '<Permission> %s' % self.title


# 用户—角色关联表
user_role = db.Table('user_role', db.metadata,
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class Role(db.Model):
    """
    角色表
    """
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))

    # 双向关联，用于跨表查询
    users = db.relationship('User', secondary=user_role, backref='roles')

    def __str__(self):
        return '<Role %s>' % self.name


class User(db.Model):
    """
    用户信息表
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

    def __str__(self):
        return '<User %s>' % self.username

# 笔记：
# 一对一关联的时候，在relationship里设置uselist为False
# 在Association-object模式中，级联删除要设置viewonly为False，待研究
