# _*_coding: utf-8 _*_
import queue

## 3. metaclass
### convert all attributes key to lower case
class lowercase_meta(type):
    def __new__(cls, name, bases, attrs):
        print(f"cls is {cls}, name is {name}, bases is {bases}, attrs is {attrs}")
        lowercase_attrs = {}
        for key, value in attrs.items():
            if not key.startswith("__") and isinstance(key, str):
                lowercase_attrs[key.lower()] = value
            else:
                lowercase_attrs[key] = value
        return super().__new__(cls, name, bases, lowercase_attrs)


class Person(object, metaclass=lowercase_meta):
    ## class attribute
    Attribute1 = "value1"
    Attribute2 = "value2"

    def __init__(self, name, age):
        # instance attribute
        self.name = name
        self.age = age


def test_metaclass():
    p1 = Person("Alice", 30)

    ## class attribute can accessd by instance
    print(p1.attribute1)
    print(p1.attribute1)
    
    print("---"*100)
    ## and also accessed by class
    print(Person.attribute1)
    Person.attribute1 = "new_value1"
    print(Person.attribute1)
    print(Person.attribute2)


## 4. overwrite __new__
### overwrite __new__ method to support singleton and add a specifc queue to instance
class Singleton:
    _instance= {}
    def __new__(cls):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__new__(cls)
            cls._instance[cls].queue = queue.Queue()
        return cls._instance[cls]



def test_singleton():
    s1 = Singleton()
    s2 = Singleton()

    assert s1 is s2, "s1 and s2 are not the same instance"
    assert s1.queue is s2.queue, "s1 and s2 queue are not the same instance"


if __name__ == "__main__":
    test_singleton()
    print("test_singleton pass")
    test_metaclass()



