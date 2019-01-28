
class Person():
    pass

p = Person()
p.name = 'ouyang'
p.age = 29
print(p.name)
print(p.age)

class Alien():
#__slots__属性限制了，alien类只能增加一个name属性，不能增加其它属性了。
    __slots__ = ('name')

a = Alien()
a.name = 'moshen'
#比如age属性，添加就会出错
#a.age = 28
print(p.name)
print(p.age)


#装饰器可以给动态加功能，使得属性既可以简单访问，又可以类型检查。
#@property装饰器，可以把一个方法变成属性调用。
class Student():

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            print('请重新输入')

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if isinstance(value, int):
            self._birth = value
        else:
            print('请重新输入数字')

#只读属性age
    @property
    def age(self):
        return 2019 - self._birth

s = Student()
s.name = 'minglong'
print(s.name)
s.birth = 2000
print(s.birth)
#只读属性，不能赋值
#s.age = 45
print(s.age)