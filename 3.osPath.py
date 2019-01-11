#os模块常用方法，处理文件夹，mkdir,rmdir,getcwd
#处理文件，rename,remove
#可以一个一个测试其用法，加深理解

import os

#os.mkdir('myTest')#新建文件夹
#os.mkdir('myTest/second')#新建文件夹
#os.chdir(r'C:\Python')#切换当前目录到参数所指目录
print(os.getcwd())#返回当前目录
#os.rmdir('myTest')#删除文件夹，但是要文件夹里面是空的，才能够删除

#打开文件，如果没有此文件，就会新建（w模式下，r模式会出错）。
files = open('myTest/second/test.txt','r+')
mes = files.read()
files.write('hello')
print(mes)
files.close()

#删除，重命名
#os.rename('myTest/second/test.txt', 'myTest/second/test2.txt')
#os.remove('myTest/second/test.txt')