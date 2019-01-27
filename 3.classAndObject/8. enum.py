from enum import Enum

Month = Enum('Monthy',('Jan', 'Feb', 'Mar'))

print(type(Month.Jan))
print(type(Month))
print(Month.__name__)
#枚举的编号从一开始。
print(Month.Jan.value)


#更精确的控制枚举，可以自定义编号
class Gender(Enum):
    Male = 0
    Female = 1

print(type(Gender.Male))
print(type(Gender))
print(Gender.Male)
print(Gender.Male.value)
print(Gender(1))