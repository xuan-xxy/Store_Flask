#商城需要数据库


# 用户表: User
id
username
pasword


#用户的收货地址表 UserArdess

user_id
address
phone_number



#商品表: Prodcuts
id
goods_name: 商品名字
goods_price: 商品价格
goods_classify: 商品分类
goods_summary: 商品概述
goods_img_url: 商品url


# 用户订单表
user_id
product_id
order_status: 订单状态
order_count: 订单数量
order_total_price: 订单总价
order_number: 订单号, 用户id + 时间戳生成
address
phone_number

订单需要添加删除功能这个实现是设置订单的一个字段, delete: 删除物理删除

#后台管理: Management




#后台管理员: ManageUser





需要完善的功能


1. 用户账号7天保持状态

2: 登录之后首页页面需要显示用户名字(完成)

3.消息闪现

4. 支付接口

5. 删除购物车里面的产品接口 (完成)

6: 收获地址的表需要添加用户name 字段(后期完善)

7. html页面需要完善并精致









