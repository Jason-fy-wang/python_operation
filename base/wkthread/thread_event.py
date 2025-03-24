import threading
import time

event = threading.Event()


def worker0():
    print("send event")
    event.set()
    print("event is set")
    time.sleep(1)
    print("clear event")
    event.clear()

def worker1():
    print("worker: waiting for event to be set")
    event.wait()  # Wait until the event is set
    print("worker: event is set, continuing work")
    while not event.is_set():
        print("worker: waiting event to continue work")
        time.sleep(1)
    print("get singal again and continue to work")



def test_event():
    t1 = threading.Thread(target=worker1)
    t1.name = "worker1"
    t1.start()

    t0 = threading.Thread(target=worker0)
    t0.name = "worker0"
    t0.start()








