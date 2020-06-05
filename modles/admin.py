# -*- coding: utf-8 -*-
#Auth:xuanxuan
from modles import db, BaseModel
"""
后台管理者

"""


class AdminUser(BaseModel):
    __tablename__ = 'admin_user'
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(100))



