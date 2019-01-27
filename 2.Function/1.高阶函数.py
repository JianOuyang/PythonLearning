from functools import reduce, partial

STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str_to_int(x):
    return STR_TO_INT[x]

def add(x, y):
    return x * 10 + y

m = reduce(add, map(str_to_int, ['1','2']))
print(m)
print(type(m))



STR_TO_TITLE = {'Z':'z','A':'a'}

def str_to_title_map(x):
    if x in STR_TO_TITLE.keys():
        return STR_TO_TITLE[x]
    else:
        return x

def str_to_title(s):
    title = list(map(str_to_title_map, s))#从迭代器变成可迭代对象
    title[0] = title[0].upper()
    title = ''.join(title)
    return title

title = str_to_title('zAzaZ')
print(title)

print(type(True))


#偏函数
sorted_reverse = partial(sorted, reverse = True)

li = [23,453,657,7,5]
li1 = sorted(li)
li2 = sorted_reverse(li)
print(li1)
print(li2)