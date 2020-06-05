# -*- coding: utf-8 -*-
#Auth:xuanxuan
from modles import db, BaseModel

"""



#商品表: Prodcuts
id
goods_name: 商品名字
goods_price: 商品价格
goods_classify: 商品分类
goods_summary: 商品概述
goods_img_url: 商品url




"""

class Goods(BaseModel):
    __tablename__ = 'goods'
    goods_name = db.Column(db.String(255))
    goods_price = db.Column(db.Integer)
    goods_classify = db.Column(db.String(255))
    goods_summary = db.Column(db.String(255))
    goods_img_url = db.Column(db.String(255))



