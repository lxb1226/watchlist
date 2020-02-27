# 创建数据库模型
# 表名将会是user(自动生成,小写处理)
# User模型继承UserMixin类
# 继承这个类会让User类拥有几个用于判断认证状态的属性和方法,其中最常用的属性是is_authenticated属性：如果当前用户已经登录,
# 那么current.is_authenticated会返回True，否则返回False
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from watchlist import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(20))

    # 用来设置密码的方法，接受密码作为参数
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # 用于验证密码的方法，接受密码作为参数
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
