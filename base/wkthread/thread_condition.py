
import threading



condition = threading.Condition()


def worker0():
    print("worker0 start")
    condition.acquire()
    print("worker0 acquired condition and begin wait signal")
    condition.wait()  # Wait until notified
    print("worker0 notified")


def worker1():
    # print("worker1 start")
    # condition.acquire()
    # print("worker1 acquired condition")
    # condition.notify()  # Notify one waiting thread
    # print("worker1 notified")
    # condition.release()
    # print("worker1 released condition")
    ## replace above code with a context manager
    with condition:
        print("worker1 acquired condition")
        condition.notify()  # Notify one waiting thread
        print("worker1 send singal")


t0 = threading.Thread(target=worker0)
t0.name = "worker0"
t0.start()

t1 = threading.Thread(target=worker1, name="worker1")
t1.start()


t0.join()
t1.join()
