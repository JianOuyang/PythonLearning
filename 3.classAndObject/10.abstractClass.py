from abc import ABCMeta, abstractmethod

#定义了一个抽象类（即接口），用到了abc里面的两个模块
class IPerson(metaclass = ABCMeta):
    @abstractmethod
    def print_name(self):
        pass

    @abstractmethod
    def print_age(self):
        pass

class Person(IPerson):

    def print_name(self):
        print('ouyang')

    #一定要把每一个抽象方法都重新，拥有抽象方法，就不能实例化
    def print_age(self):
        print(34)

p = Person()
p.print_name()
print(isinstance(p, IPerson))

#抽象类的目的就是让别的类继承它并实现特定的抽象方法