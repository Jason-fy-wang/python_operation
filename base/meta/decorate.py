# _*_coding: utf-8 _*_

from functools import wraps
import random
import time
## 1. function decorate
def log_info(func):

    def wrapper(*args, **kwargs):
        print("start")
        now = time.time()
        result = func(*args, **kwargs)
        print(f"end: {time.time() - now}")
        return result
    return wrapper


def record_info(min, max):

    def record_operation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # mock record into database
            val = random.randint(min, max)
            now = time.time()
            time.sleep(val)
            print("record start")
            func(*args, **kwargs)
            print(f"record end: {time.time() - now}")
        return wrapper
    return record_operation


## 2. class decrate
class persist_record_into_db:

    def __init__(self):
        pass

    def __call__(self, func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # mock record into database
            now = time.time()
            print("persist record start")
            func(*args, **kwargs)
            print(f"persist record end: {time.time() - now}")
        return wrapper


@log_info
def long_time_calc():
    """A function that takes a long time
    """
    time.sleep(1)
    print("long time calc")

@record_info(1,10)
def long_time_calc2():
    """A function that takes a long time
    """
    time.sleep(1)
    print("long time calc2")


@persist_record_into_db()
def long_time_calc3():
    """A function that takes a long time
    """
    time.sleep(1)
    print("long time calc3")


if __name__ == "__main__":
    long_time_calc()
    long_time_calc2()
    long_time_calc3()





