# -*- coding: utf-8 -*-
#Auth:xuanxuan
import os
from flask_migrate import MigrateCommand
from flask_script import Manager
from app import create_app
from modles import *
from modles.user import *
from modles.product import *
from modles.admin import *

env = os.environ.get("FLASK_ENV", "develop")
app = create_app(env)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # 运行命令: python manager.py runserver
    # 数据库初始化:python manager.py db init
    # 数据库迁移:python manager.py db migrate
    # 数据库迁移命令完之后该使用数据库更新命令：python manager.py db upgrade
    manager.run()