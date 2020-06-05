# -*- coding: utf-8 -*-
#Auth:xuanxuan
from flask import Flask, session

from settings import envs
from modles import init_db
from app.user import user_bp
from app.order import order_bp

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_db(app)
    app.register_blueprint(user_bp)
    app.register_blueprint(order_bp)


    return  app