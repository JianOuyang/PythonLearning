#内存中存储
from io import StringIO, BytesIO

f = StringIO()
f.write('欧阳\n')
f.write('聊天宝')
result = f.getvalue()
print(result)

fb = BytesIO()
fb.write('欧阳\n'.encode('utf-8'))
fb.write('欧阳'.encode('GBK'))
print(fb.getvalue())
print(fb.getvalue().decode('utf-8', errors='ignore'))

#操作系统
import os

print(os.name)
print(os.path.abspath('.'))
print(os.getcwd())
filename = os.path.join('.','TEST2')
#os.mkdir(filename)
#os.rmdir(filename)

filename2 = os.path.split(filename)#把最后级别的文件或目录分离出来。
filename3 = os.path.splitext(filename)#把文件的扩展名提取出来。
print(filename2)
print(filename3)


#常用写入文件
with open('somefile1.txt', 'wt') as f:
    f.write('line1\n')
    f.write('line2')
#打印输出到文件中
with open('somefile.txt', 'w') as f:
    print('line1', file=f)
    print('line2', file=f)

print(os.path.exists('somefile1'))
print(os.path.isfile('somefile1'))


# Get all regular files
names = [name for name in os.listdir('somefile')
        if os.path.isfile(os.path.join('somefile', name))]

print(names)

# Get all dirs
dirnames = [name for name in os.listdir('somefile')
        if os.path.isdir(os.path.join('somefile', name))]

print(dirnames)