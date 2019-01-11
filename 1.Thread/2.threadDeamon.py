"""
后台线程的责任是为整个主线程提供服务,如保持
网络连接(发送keep-alive心跳包),负责内存管理
与垃圾回收(实际上JVM就是这样做的). 因此这些线程
与实际提供应用服务的线程有了逻辑上的”前/后”的概念,
而如果主线程已经退出,那么后台线程也没有存在的必要. 

如果没有这一机制,那么我们在主线程完成之后,
还必须逐个地检查后台线程,然后在主线程退出之前,
逐个地关闭它们. 有了前后线程的区分, 我们只需要负责
管理前台线程, 完成主要的逻辑处理之后退出即可.

"""

import threading
import time
import random

lock = threading.Lock()

def show():
	print('第一个子线程' + time.ctime())
	time.sleep(random.randrange(1,4))
	print('第一个子线程结束' + time.ctime())

def show2():
	print('第二个子线程' + time.ctime())
	time.sleep(random.randrange(1,4))
	print('第二个子线程结束' + time.ctime())
	
def main():
	#多线程
	threads = []	
	print('主线程开始' + time.ctime())
	time.sleep(1)
	thread1 = threading.Thread(target = show2)
	thread2 = threading.Thread(target = show)
	threads.append(thread1)
	threads.append(thread2)
	#线程同时启动
	for thread in threads:
		thread.setDaemon(True)#设置线程为后台线程
		thread.start()
	print('主线程结束' + time.ctime())

if __name__ == '__main__':
	main()