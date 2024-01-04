from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def my_abstract_method(self):
        pass

    @staticmethod
    def concrete_method():
        print("This is a concrete method")


# This class inherits from MyAbstractClass and implements my_abstract_method
class ConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        print("Implemented abstract method")


if __name__ == "__main__":

    # Attempting to instantiate MyAbstractClass will raise an error
    # abstract_instance = MyAbstractClass()  # This would raise TypeError

    # Instantiating ConcreteClass works fine
    concrete_instance = ConcreteClass()
    concrete_instance.concrete_method()
    concrete_instance.my_abstract_method()  # Implemented abstract method
