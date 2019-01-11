"""
open 函数有三个参数，file_name，access_mode，buffering.常用的是前两个参数。
file_name代表的参数就是文件地址，可以是相对地址，也可以是绝对地址。
access_mode是指打开文件的方式是什么，只读r，只写w，读写r+，二进制只读rb。。。。

打开文件了，常用方法有read,write,close
常用属性有closed,mode,name,
"""

import os 

filename = r'C:\Users\212669006\Desktop\test.txt'

def check_file(filename):
	while os.path.isfile(filename):
		try:
			with open(filename, 'rb+') as f:
				files = f.read()
				print(files)
				#如果是用二进制格式打开文件，需要解码
				#记事本保存为什么格式编码就用什么格式解析
				#记事本一般有4种编码格式，ANSI，UTF-8,UNICODE,UNICODE BIG ENDIAN
				print(files.decode('ANSI'))
				f.close()
				print(f.name)
		except:
			print('the file is not exist')
		break
def main():
	check_file(filename)

if __name__ == '__main__':
	main()
