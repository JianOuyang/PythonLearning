#如果你想对一个attribute进行自定义的验证。例如类型检查，数值是否在范围内等等

class person:
	def __init__(self, firstname, age):
		self.firstname = firstname
		self.set_age(age)

#第一步，创建property方法（firstname的getter函数），使firstname变成一个属性。
#只有这一步把firstname变成属性之后，后面两个函数才有意义。
	@property
	def firstname(self):
		return self._firstname

#第二步，创建firstname的setter函数，对属性的赋值进行类型检查。
#如果不是str类型，就报错。下面示例，赋值22就会引发错误。
	@firstname.setter
	def firstname(self, value):
		if isinstance(value, str):
			self._firstname = value
		else:
			raise TypeError('expected str type')

#可选的property方法deleter。保证该属性不能被删除，或者删除的时候做一些处理
	@firstname.deleter
	def firstname(self):
		print('the property will be delete')
		#raise AttributeError('the attribute can not be delete')


	def get_age(self):
		return self._age

	def set_age(self, value):
		if isinstance(value, int) and value > 0 and value < 100:
			self._age = value
		else:
			print('the age in not right')

	name = property(get_age, set_age)

p = person('moshen', 400)
print(p.firstname)
#p.firstname = 22
p.firstname = 'minglong'
print(p.firstname)
del p.firstname
print(p.firstname)
print(p.get_age())