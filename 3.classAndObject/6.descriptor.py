
#定义了一个描述器，这个描述器的功能是限制该类型只能是整数。
#通过实现get，set，delete三个方法实现。
class Integer:
	def __init__(self, num):
		self.num = num

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			return instance.__dict__[self.num]

	def __set__(self, instance, value):
		if not isinstance(value, int):
			raise TypeError('Expected an int')
		instance.__dict__[self.num] = value

	def __delete__(self, instance):
		del instance.__dict__[self.num]

class ClassName:
	"""docstring for ClassName"""
	#描述器只能在类的级别定义，而不能在每个实例定义，也就是不能在init函数里面定义
	age = Integer('age')

	def __init__(self, age):
		self.age = age

c = ClassName(12)
c.age = 25
print(c)
