
class Base:
	def __init__(self):
		print('这是基类的初始化')

class childA(Base):
	def __init__(self):
		super().__init__()
		print('这是基类A的初始化')

class childB(Base):
	def __init__(self):
		super().__init__()
		print('这是基类B的初始化')

class childC(childA, childB):
	def __init__(self):
		super().__init__()
		print('这是基类C的初始化')

#会按照方法解析顺序表（MRO）调用父类的方法。
#MRO顺序是childC-childA-childB-base
#MRO顺序原则：子类在父类前面（先childC）；并列的父类，先继承的在前面（childA在childB前面）；
c = childC()