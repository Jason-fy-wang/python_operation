
import threading
import queue
import time

def producer(queue):
    for i in range(1, 11):
        queue.put(i)
        print(f"producer: produced {i}")
        time.sleep(1)

def consumer(queue):
    for i in range(1, 11):
        item = queue.get()
        print(f"consumer: consumed {item}")
        time.sleep(1)

queue = queue.Queue(maxsize=2)

t0 = threading.Thread(target=producer,name="producer", args=(queue,))
t1 = threading.Thread(target=consumer, args=(queue,), name="consumer")
t0.start()
t1.start()

t0.join()
t1.join()
