# -*- coding: utf-8 -*-
#Auth:xuanxuan
import pymysql
import datetime
import random

_list =['https://img10.360buyimg.com/n7/jfs/t1/124212/9/3462/192563/5ed1e0dfEecfc34f7/68f5d63c18b1bfb7.jpg',
        'https://img14.360buyimg.com/n7/jfs/t1/101336/38/6885/169735/5df7a30dEff8aad5f/44b12c05f5f43bfe.jpg',
        'https://img12.360buyimg.com/n7/jfs/t1/112449/15/4713/125946/5eafddacE08bc66e0/70c49b2d7b39e64f.jpg',
        'https://img10.360buyimg.com/n7/jfs/t1/133730/29/956/242158/5ed3e36eEcf035119/515a9455a7a37718.jpg',
        'https://img10.360buyimg.com/n7/jfs/t1/93410/11/18680/75647/5e98245aEc4976a79/8a8a4ece38f41e1e.jpg',
        'https://img13.360buyimg.com/n7/jfs/t1/131841/16/886/178710/5ed329e9E8c2a9e18/70e825b31a2b80db.jpg',
        'https://img12.360buyimg.com/n7/jfs/t1/23031/13/4929/129940/5c37c6a4E1a755eeb/b90a1b8d1d4ed3c2.jpg',
        'https://img14.360buyimg.com/n7/jfs/t1/105321/5/17172/166132/5e855cb7E7abdcc91/dd71b51653aba9c9.jpg',
        'https://img13.360buyimg.com/n7/jfs/t1/131443/37/1081/240722/5ed5a0a2E2693aace/c540764e323139d8.jpg',
        'https://img13.360buyimg.com/n7/jfs/t1/92542/28/12804/120107/5e4fe1f6E4297394a/f1c6727619d50e22.jpg',
        'https://img13.360buyimg.com/n7/jfs/t1/125496/34/599/160384/5eb64f58E5500a3b3/b5fc4b145d438f0e.jpg',
        'https://img13.360buyimg.com/n7/jfs/t1/129556/15/3728/159804/5ed5c4fcEab11e94b/3841c66a4187ce40.jpg',
        'https://img14.360buyimg.com/n7/jfs/t1/117425/38/8296/154458/5ecce2cdE3ba84df9/6e07de93d4fc787d.jpg',
        'https://img14.360buyimg.com/n7/jfs/t1/134717/16/26/157067/5ec796cfEd9dbb7a8/179b1e0282785fae.jpg',
        'https://img10.360buyimg.com/n7/jfs/t1/14014/33/10075/201233/5eb65b11Ead84e7c4/244c2f713a8dd41d.jpg',
        'https://img13.360buyimg.com/n7/jfs/t1/110324/32/13163/183730/5e9e507fEcd2cdff5/b18a84c018f8b53c.jpg',
        'https://img13.360buyimg.com/n7/jfs/t1/96112/26/13710/191225/5e5bb08fEf3baa45f/4d5a01e2467ab6b7.jpg',

        ]






def get_conn():
   db= pymysql.connect(host='localhost', user="root",
                     password='123456', db='store', charset='utf8', port=3306, cursorclass=pymysql.cursors.DictCursor)
   return db

def sql_excute(sql):
   db = get_conn()
   cur = db.cursor()
   try:
      print("insert")
      cur.execute(sql)   #执行sql语句
      db.commit()
   except Exception as e:
      print(e)
      db.rollback()
   finally:
      db.close()

def query(sql):
   results = None
   db = get_conn()
   cur = db.cursor()
   try:
      print(sql)
      cur.execute(sql)
      #执行sql语句
      results = cur.fetchall()   #获取查询的所有记录
      return results
   except Exception as e:
      raise e
   finally:
      db.close()

def q(i):
   if isinstance(i,int) or isinstance(i,float):
      return str(i)
   elif isinstance(i,datetime.datetime):
      return str(int(i.timestamp()))
   else:
      return pymysql.escape_string(i)

def insert_mysql(insertObj):
    k_list = []
    v_list = []
    for k in insertObj.keys():
        k_list.append(k)
        v_list.append(q(insertObj[k]))
    sql = "INSERT INTO `goods`(`{}`)VALUES('{}')".format('`,`'.join(k_list), '\',\''.join(v_list))
    sql_excute(sql)

def sql_update(updateObj):
    update_str = []
    unit = "`{}`='{}'"
    for k in updateObj.keys():
            unit_str = unit.format(k, str(updateObj[k]))
            if "_id" in unit_str:
                unit_str2=unit_str.split("=")[1]
                unit_str="id"+"="+unit_str2
            update_str.append(unit_str)
    sql = "UPDATE `aggregation` SET {} WHERE `id` = '{}'".format(','.join(update_str),updateObj['_id'])
    sql_excute(sql)


if __name__ == '__main__':
    for url in _list:
        _dict = {}
        _dict['goods_name'] = '女生短袖{}'.format(random.choice(['学生', '青年', '少年', '流行', '中年']))
        _dict['goods_price'] = random.choice([20, 39, 49, 50, 35, 70, 100])
        _dict['goods_classify'] = 'Tshit'
        _dict['goods_summary'] = '美丽女生, 美丽心情'
        _dict['goods_img_url'] = url
        insert_mysql(_dict)
