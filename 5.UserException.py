
class MyException(Exception):
    pass


def fn():
    try:
        age = 900
        if age > 0 and age < 100:
            print(age)
        else:
            #自定义的异常一定要自己raise，异常信息也可以自定义
            raise MyException('请确认输入合适的年龄。')
    except MyException as e:
        print(e)
        raise MyException('这个问题我搞不定，我传给你（main）了，你来处理。')


def main():
    try:
        fn()
    except MyException as e:
        print(e)
        print('好的，你（fn）处理不了，我来搞定！！！')

#main()


#记录错误信息 logging
import logging
logging.basicConfig(level = logging.DEBUG)

try:
    age = 900 / 0
    print(age)
except Exception as e:
    logging.exception(e)
    print('end')