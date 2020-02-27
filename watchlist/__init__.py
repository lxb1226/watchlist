import os
import sys

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 设置签名所学要的密钥
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
# 设置数据库URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



@login_manager.user_loader
# 创建用户加载回调函数,接受用户ID作为参数
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user





# 模板上下文处理函数
@app.context_processor
# 函数名可以随意修改
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    # 需要返回字典，等同于return {'User':user}
    return dict(user=user)


from watchlist import views, errors, commands
