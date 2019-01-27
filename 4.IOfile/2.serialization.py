import json
import pickle

a = dict(name = 'ouyang', phone = 'honor')
a1 = {'name': 'ouyang', 'phone': 'honor'}

b = json.dumps(a)
print(b)
print(type(b))
c = json.loads(b)
print(c)
print(type(c))

# with open('test.txt', 'a') as f:
#     f.write(json.dumps(a) + '\n')


#序列化对象
class Student(object):
    """docstring for Student"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

def stu2json(student):
    return {
        'name': student.name,
        'age': student.age
    }

def json2stu(di):
    return {Student(di['name'], di['age'])}

s = Student('ouyang', '99')
b = pickle.dumps(s)
print(b)
print(type(b))

c = pickle.loads(b)
print(c.age)
print(type(c))


#pickle模块
import pickle

s = Student('ouyang', '99')
with open('somefile.txt', 'rb') as f:
    #b = pickle.dump(s, f)
    b = pickle.load(f)
    print(b.age)

