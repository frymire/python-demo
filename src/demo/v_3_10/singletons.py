class BaseSingleton:

    instances = {}
    name: str

    def __new__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__new__(cls)
        return cls.instances[cls]

    def __init__(self):
        print("In __init__()")
        if not hasattr(self.__class__, '_initialized'):
            self.initialize()
            self.__class__._initialized = True

    @staticmethod
    def initialize():
        print("In _initialize()")

    def speak(self) -> str:
        return f"I am {self.name}"


class Child1(BaseSingleton):

    def __init__(self):
        super().__init__()
        self.name = "Child1"


class Child2(BaseSingleton):

    def __init__(self):
        super().__init__()
        self.name = "Child2"


a1 = Child1()
a2 = Child1()  # __init__ will be skipped
b1 = Child2()
b2 = Child2()  # __init__ will be skipped

print(a1.speak())  # "I am Child1"
print(a2.speak())  # "I am Child1"
print(a1 is a2)  # True

print(b1.speak())  # "I am Child2"
print(b2.speak())  # "I am Child2"
print(b1 is b2)  # True

print(a1 is b1)  # False
