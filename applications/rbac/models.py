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
                           db.Column('permission_id', db.Integer,
                                     db.ForeignKey('permission.id', ondelete='CASCADE', onupdate='CASCADE')),
                           db.Column('role_id', db.Integer,
                                     db.ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE'))
                           )


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
    roles = db.relationship('Role', secondary=permission_role, passive_deletes=True)

    def __str__(self):
        return '<Permission> %s' % self.title


# 用户—角色关联表
user_role = db.Table('user_role', db.metadata,
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),
                     db.Column('role_id', db.Integer, db.ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE'))
                     )


class Role(db.Model):
    """
    角色表
    """
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))

    # 多对多的双向关联，用于跨表查询
    permissions = db.relationship('Permission', secondary=permission_role, passive_deletes=True)
    users = db.relationship('User', secondary=user_role, passive_deletes=True)

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

    # 多对多的双向关联，用于跨表查询
    roles = db.relationship('Role', secondary=user_role, passive_deletes=True)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

    def __str__(self):
        return '<User %s>' % self.username

# 笔记：
# 一对一关联的时候，在relationship里设置uselist为False
# 在Association-object模式中，级联删除要设置viewonly为False，待研究
# 级联删除的实现方式之一：在Foreign中添加ondelete='CASCADE', onupdate='CASCADE'，在relationship中添加passive_deletes=True
