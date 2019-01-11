import threading
import time

def show():
	print('第一个线程' + time.ctime())
	time.sleep(1)
	print('第一个线程结束' + time.ctime())

def show2():
	print('第二个线程' + time.ctime())
	time.sleep(3)
	print('第二个线程结束' + time.ctime())

def main():	
	#直接调用，按顺序执行函数，串行
	# show()
	# show2()
	#多线程
	threads = []	
	print('主线程开始' + time.ctime())
	time.sleep(1)
	thread1 = threading.Thread(target = show)
	thread2 = threading.Thread(target = show2)
	threads.append(thread1)
	threads.append(thread2)
	#两个线程同时启动
	for thread in threads:
		thread.start()
	#阻塞主线程，等两个线程都执行完了才执行主线程
	for thread in threads:	
		thread.join()
	#time.sleep(2)
	print('主线程结束' + time.ctime())

if __name__ == '__main__':
	main()