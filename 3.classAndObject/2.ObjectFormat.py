#重写__format__函数，实现不同环境下（中国，美国），以不同的格式显示对象


class name:
	def __init__(self, lastname, firstname):
		self.lastname = lastname
		self.firstname = firstname

	def __format__(self, country):
		if country == 'China':
			return '我的名字是{0.firstname}{0.lastname}'.format(self)
		elif country =='American':
			return 'My name is {0.lastname} {0.firstname}'.format(self)
		else:
			return 'Wrong country'

	def __enter__(self):
		print('开始with控制流')

	def __exit__(self, exc_ty, exc_val, tb):
		print('with控制流结束了')


n = name('吹雪','西门')
print(format(n, 'China'))
print(format(n, 'American'))

#实现with控制流，重写enter和exit方法。保证在执行某些操作之前该做什么（enter函数）
#保证某些操作结束之后该做什么（exit函数，有4个参数）
with n:
	b= 120
	print(b)

print(n)

