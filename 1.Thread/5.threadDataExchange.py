import queue
import threading
import random
import time

lock = threading.Lock()

def producer(q):
	while True:
		evt = threading.Event()
		data = random.randrange(1,4)
		q.put((data,evt))
		print('插入' + str(data))
		evt.wait()
		print('消费者已经收到数据')

def consumer(q):
	while True:
		try:
			data, evt = q.get(block = False)
			print(data)
			evt.set()
		except queue.Empty:
			print('the queue is Empty')


q = queue.Queue()
t1 = threading.Thread(target=consumer, args=(q,))
t2 = threading.Thread(target=producer, args=(q,))
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
time.sleep(0.1)
print('结束')



#测试队列的非阻塞方式和设定超时
# q = queue.Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# try:
# 	while True:
# 		print(q.get(timeout = 0.5))
# except queue.Empty:
# 	print('the queue is Empty')

# try:
# 	while True:
# 		print(q.get(block = False))
# except queue.Empty:
# 	print('the queue is Empty')