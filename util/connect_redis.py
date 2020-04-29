import redis
r = redis.Redis(host='127.0.0.1',port=6379,password='test123')
value = r.set("name","xuexi")
key = r.get("name").decode('utf8')
print(key)
r.close()

'''
连接池
'''
pool = redis.ConnectionPool(host='127.0.0.1',password='test123')
r = redis.Redis(connection_pool=pool)
r.set('foo','bar')
print(r.get('foo').decode('utf8'))
r.close()


