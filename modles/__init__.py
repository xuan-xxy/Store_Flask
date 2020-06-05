# -*- coding: utf-8 -*-
#Auth:xuanxuan
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE': 'redis'})

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)



class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e, '插入数据库错误')
            return False
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            return False


