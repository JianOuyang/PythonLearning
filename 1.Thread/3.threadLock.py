import threading
import time
import random

lock = threading.Lock()

def show():
	with lock:
		print('第一个子线程' + time.ctime())
		time.sleep(random.randrange(1,4))
		print('第一个子线程结束' + time.ctime())

def show2():
	with lock:
		print('第二个子线程' + time.ctime())
		time.sleep(random.randrange(1,4))
		print('第二个子线程结束' + time.ctime())
	
def show3():
	print('第三个子线程' + time.ctime())
	time.sleep(random.randrange(1,4))
	print('第三个子线程结束' + time.ctime())

def main():	
	#直接调用，按顺序执行函数，串行
	# show()
	# show2()
	#多线程
	threads = []	
	print('主线程开始' + time.ctime())
	time.sleep(1)
	#三个函数都加锁了，先加到list里面的先执行，这就和串行一样了，是单线程	
	#锁两个函数，这两个函数执行有先后顺序，是单线程。
	#相当于这两个函数是一个线程，另外一个函数是一个线程
	thread1 = threading.Thread(target = show2, daemon=True)
	thread2 = threading.Thread(target = show, daemon=True)
	thread3 = threading.Thread(target = show3, daemon=True)
	threads.append(thread1)
	threads.append(thread2)
	threads.append(thread3)
	#线程同时启动
	for thread in threads:
		thread.start()
	#阻塞主线程，等子线程都执行完了才执行主线程
	for thread in threads:
		thread.join()
	print('主线程结束' + time.ctime())

if __name__ == '__main__':
	main()