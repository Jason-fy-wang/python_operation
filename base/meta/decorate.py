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


class sleep_while_before_execute:
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Decorator that sleeps for a given time before executing the function.
            """
            time.sleep(self.sleep_time)
            return func(*args, **kwargs)
        return wrapper
    

class sleep_without_wrapper_while_before_execute:
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            """Decorator sleep_without_wrapper_while_before_execute that sleeps for a given time before executing the function.
            """
            time.sleep(self.sleep_time)
            return func(*args, **kwargs)
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

@sleep_while_before_execute(2)
def long_time_calc4():
    """A function4 that takes a long time
    """
    time.sleep(1)
    print("long time calc4")

@sleep_without_wrapper_while_before_execute(2)
def long_time_calc5():
    """A function5 that takes a long time
    """
    time.sleep(1)
    print("long time calc5")

if __name__ == "__main__":
    # long_time_calc()
    # long_time_calc2()
    # long_time_calc3()
    # long_time_calc4()
    print(long_time_calc4.__name__)
    print(long_time_calc4.__doc__)
    print("*"*20, "func5", "*"*20)
    print(long_time_calc5.__name__)
    print(long_time_calc5.__doc__)




