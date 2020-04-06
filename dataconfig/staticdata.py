#conding:utf-8
#登录接口
url = 'http://127.0.0.1/api/mgr/signin'
data = {
    "username": "byhy",
    "password": 88888888
}
header = {
    "Content-Type": "application/x-www-form-urlencoded"
}
#获取用户列表接口
url1 = 'http://127.0.0.1/api/mgr/customers'
params1 = {
    'action': 'list_customer',
    'pagesize': 10,
    'pagenum': 1,
    'keywords': '',
}
header1 = {
    "Content-Type": "application/json",
    "Cookie": "sessionid=6wqk09ziylur427rre8p4p4t15wwtp9z"
}
#添加用户
url2 = "http://127.0.0.1/api/mgr/customers"
data2 ={
    "action":"add_customer",
    "data":{
        "name":"杭州市第二医院",
        "phonenumber":"13345679934",
        "address":"杭州市第二医院北路"
    }
}
header2 ={
    "Content-Type":"application/json",
    "Cookie":"sessionid=ldx3bark4n5urpmss2ecy76r81mxxhxw"
}
#修改用户
url3 = "http://127.0.0.1/api/mgr/customers"
data3 = {
    "action":"modify_customer",
    "id": 43,
    "newdata":{
        "name":"武汉市桥北医院",
        "phonenumber":"13345678888",
        "address":"武汉市桥北医院北路"
    }
}
header3 ={
    "Content-Type":"application/json",
    "Cookie":"sessionid=ldx3bark4n5urpmss2ecy76r81mxxhxw"
}