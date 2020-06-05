# -*- coding: utf-8 -*-
#Auth:xuanxuan
from flask import Blueprint, request, render_template, redirect, url_for, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import functools
from modles.user import User, UserArdess

"""

用户登录, 注册, 登出页面
"""


user_bp = Blueprint('user', __name__, template_folder='D:/Store/templates', static_folder='D:/Store/static')
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username:
            result = User.query.filter(User.username == username).first()
            if result:
                password_hash = generate_password_hash(password)
                if check_password_hash(password_hash, password):
                    session.permanent = True
                    session['username'] = username
                    session['user_id'] = result.id
                    g.username = username
                    return redirect(url_for('order.index'))
            else:
                return redirect(url_for('user.register'))
    return render_template('user/login.html')


@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html')
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    user = User()
    if username:
        user.username = username
        user.password = generate_password_hash(password)
        if user.save():
            return redirect(url_for('user.login'))

    return render_template('user/register.html')


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('user.login'))


#用户登录验证, 一些操作需要在登陆状态才能操作
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('username') is None:
            return redirect(url_for('user.login'))
        return view(**kwargs)
    return wrapped_view



@login_required
@user_bp.route('/useraddress', methods=['GET', 'POST'])
def user_address():
    if request.method == 'POST':
        user_id = session['user_id']
        address = request.form.get('address')
        phone_number = request.form.get('phone')
        user_address = UserArdess()
        user_address.user_id = user_id
        user_address.address = address
        user_address.phone_number = phone_number
        print(phone_number, address, '收获地址的保存' )
        if user_address.save():
            return redirect(url_for('order.add_order'))

    return render_template('user/address.html')



