# -*- coding: utf-8 -*-
#Auth:xuanxuan
from modles import db, BaseModel
"""
用户信息表

# 用户订单表
user_id
product_id
order_status: 订单状态 : 默认是0: 未支付, 1: 支付完成, 
order_count: 订单数量
order_total_price: 订单总价
order_number: 订单号, 用户id + 时间戳生成
#后台管理: Management
"""



class User(BaseModel):
    __tablename__ = 'user'
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(100))


#收获地址
class UserArdess(BaseModel):
    __tablename__ = 'user_address'
    user_id = db.Column(db.Integer)
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))



class Order(BaseModel):
    __tablename__ = 'orders'
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    order_status = db.Column(db.Integer)
    order_count = db.Column(db.Integer)
    order_total_price = db.Column(db.Integer)
    order_number = db.Column(db.String(255), unique=True)
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))