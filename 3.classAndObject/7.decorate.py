from functools import wraps

def log(fun):
    @wraps(fun)#保留原函数的信息
    def wrapper():
        print('开始执行：{0}'.format(fun.__name__))
        fun()
    return wrapper

def run():
    print('开始跑步')

@log
def walk():
    print('开始走路')

# r = log(run)
# r()
# print(r.__name__)

# #装饰器@log的目的就是执行了log(walk)这一步。因此可以直接调用walk，而不需要像上面一样调用两个函数。
# #walk=log(walk),这一步已经完成了
# walk()

# walk.__wrapped__()#执行被包装的函数没有包装时的动作，相当于解除了装饰器


#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#具体怎么用在项目中，还得探索


#带参数的装饰器

import logging

def logged(level, name = None, message = None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def warpper(*args, **kwargs):
            log.log(level, logmsg)
            func(*args, **kwargs)
        return warpper
    return decorate

@logged(logging.ERROR)
def show(name):
    print(name)

@logged(logging.ERROR)
def attack(boss, leader):
    print('{0}正在打{1}'.format(leader, boss))

show('ouyang')
attack('大菠萝', 'ouyang')