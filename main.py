# 1-masala
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def get_animal(name):
    return Dog() if name=="dog" else Cat()
# 2-masala
class Temp:
    def __init__(self, c):
        self._c = c

    @property
    def c(self):
        return self._c
# 3-masala
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def total(cls):
        return cls.count
# 4-masala
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()
# 5-masala
class Math:
    @staticmethod
    def add(a, b):
        return a + b
