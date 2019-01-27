#生成一个类的时候就是调用了type函数。
class C(object):
    def __init__(self, name = 'dahuangfeng'):
        self.name = name

    def run(self, v = 100):
        print('速度很快，是{0}米每秒'.format(v))

    def fly(self, v = 1000):
        print('速度非常快，是{0}米每秒'.format(v))

c = C()
c.run()
c.fly()
print(c.name)
print(C.__name__)

#定义两个函数用于type函数
def run(self, v = 100):
    print('速度很快，是{0}米每秒'.format(v))

def fly(self, v = 1000):
    print('速度非常快，是{0}米每秒'.format(v))

#上面用class关键字声明了一个类，和直接用type函数生成一个类是一样的
#type函数的参数有三个，第一个是函数名，第二个是继承的父类元组，第三个是属性和参数的字典
C = type('Car', (object,), dict(car_run = run, car_fly = fly, name = 'dahuangfeng'))

c = C()#C是类的名称，我觉得是这个类的容器
c.car_run()
c.car_fly()
print(C.__name__)#Car是这个C类容器的__name__内置属性
print(c.name)#用户自定义的属性


class MylistMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        attrs['show'] = lambda self, value: print(value)
        attrs['fly'] = fly
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = MylistMetaClass):
    pass

ml = MyList()
ml.append(1)
ml.add(2)
print(ml)
ml.show('又加了一个函数')
ml.fly()