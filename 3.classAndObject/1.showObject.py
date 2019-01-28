#自定义__str__函数，输出更有用的信息，根据需求自定义输出
#自定义__repr__函数可以有相同的用途，但是有不同点，一般用于调试阶段


#str() 与 repr() 的不同在于：
#str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
#repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。
from datetime import datetime
t = datetime.now()
print(str(t))
print(repr(t))


class point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return '这是自定义输出，这个对象代表一个点：' + str((self.x, self.y))

	def __repr__(self):
		return 'point({0.x},{0.y})'.format(self)


p = point(1, 2)
print(str(p))
print(repr(p))