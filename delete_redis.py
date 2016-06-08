import redis


def deleteRedis(key):
	"""
	  需要安装redis模块，redis 没有批量删除命令，用python 循环删除,参数key在redis中可以模糊查询
	"""
	#连接redis 实例
	#db : 需要查询的redis 库
	# return list
	getRedisObject = redis.Redis(host = 'localhost',port = 6379,db = )
	keys = getRedisObject.keys(key)
	for k in keys:
		print(getRedisObject.get(k))
		getRedisObject.delete(k)