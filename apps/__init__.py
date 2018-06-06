# coding:utf-8
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
import os

db=SQLAlchemy()
basedir=os.path.abspath(os.path.dirname(__file__))

login_manager= LoginManager()
login_manager.login_view='main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #注册蓝图
    from apps.blog import  blog
    app.register_blueprint(blog)

   #注册db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
    db.init_app(app)


    #注册flask-admin
    admin = Admin(app,name="chun",template_mode='bootstrap3',base_template='admin/mybase.html')
    from .models import User,Tag,Article
    from flask_admin.contrib.sqla import ModelView
    from apps.modelview import UModelview,BaseMView,ArticleVModel

    admin.add_view(UModelview(User, db.session, name="用户管理"))
    admin.add_view(BaseMView(Tag,  db.session, category='Models' ,name="标签管理"))
    admin.add_view(ArticleVModel(Article, db.session,category='Models' , name="文章管理"))

   #整合flask-login
    login_manager.init_app(app)


    return app
