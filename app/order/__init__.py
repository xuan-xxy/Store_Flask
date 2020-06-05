# -*- coding: utf-8 -*-
#Auth:xuanxuan
from flask import Blueprint, request, render_template, redirect, url_for, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
from modles.user import User, UserArdess, Order, UserArdess
from modles.product import Goods
import datetime
from utils.config import datetime_toTimestamp
from app.user import login_required
from sqlalchemy import and_
import time
from modles import db

"""
商品展示, 用户下订单

"""

order_bp = Blueprint('order', __name__, template_folder='D:/Store/templates', static_folder='D:/Store/static')


@order_bp.route('/', methods=['GET'])
def index():
    goods_list = Goods.query.all()
    g.username = session.get('username')
    return render_template('user/index.html', goods_list=goods_list)




@order_bp.route('/search', methods=['GET', 'POST'])
def search():
    keyword = request.args.get('keyword')
    return keyword


"""
# 用户订单表
user_id
product_id
order_status: 订单状态 : 默认是0: 未支付, 1: 支付完成, 
order_count: 订单数量
order_total_price: 订单总价
order_number: 订单号, 用户id + 时间戳生成
"""


@login_required
@order_bp.route('/add_order')
def add_order():
    good = request.args.get('good_id')
    user_id = session.get('user_id')
    order_status = 0
    order_number = str(user_id) + str(datetime_toTimestamp())
    user_address = UserArdess.query.filter(UserArdess.user_id == user_id).first()
    if user_address:
        address = user_address.address
        phone_number = user_address.phone_number
    else:
        #没有收货地址, 需要创建收货地址
        return redirect(url_for('user.user_address'))
    order = Order()
    data = Goods.query.filter(Goods.id == good).all()
    order.user_id = user_id
    order.product_id = good
    order.order_count = len(data)
    order.order_status = order_status
    order.order_number = order_number
    order.order_total_price = sum([i.goods_price for i in data])
    order.address = address
    order.phone_number = phone_number
    if order.save():
           return redirect(url_for('order.index'))
    return redirect(url_for('order.index'))



@login_required
@order_bp.route('/order_deail', methods=['GET', 'POST'])
def order_detail():
    user_id = session['user_id']
    order_list = Order.query.filter(Order.user_id == user_id).all()
    if order_list:
        return render_template('user/orderdeail.html', order_list=order_list)
    flash("购物车为空")
    return redirect(url_for('order.index'))




@login_required
@order_bp.route('/delete_order', methods=['GET'])
def delete_order():
    user_id = request.args.get('user_id')
    product_id = request.args.get('product')
    print(request.args)
    print( user_id, product_id)
    result = Order.query.filter(and_(Order.user_id == user_id, Order.product_id == product_id)).first()
    print(result, '结果')
    if result:
            print('-----', result)
            db.session.delete(result)
            db.session.commit()
            return redirect(url_for('order.order_detail'))
    else:
        flash('没有该物品, 或者删除失败')
        return '删除操作失败'









@login_required
@order_bp.route('/pay', methods=['GET', 'POST'])
def pay():
    return '支付宝支付'


