from abc import abstractmethod
from typing import TypeVar, Generic


class Food:
    @abstractmethod
    def eat(self):
        print("Eating food...")


class Bamboo(Food):
    def eat(self):
        print("Eating bamboo...")


T_Food = TypeVar('T_Food', bound=Food)  # T_Food must be a subtype of Food


class Animal(Generic[T_Food]):
    def eat(self, food: T_Food) -> None:
        food.eat()


class Panda(Animal[Bamboo]):

    # If we declared "class Panda(Animal)", this method signature would violate LSP, because it would override
    # the parent signature while tightening the parameter type. By declaring "class Panda(Animal[Bamboo])", we're saying
    # that Panda is a child of Animal[Bamboo], rather than just Animal. Since Animal is now parameterized by type for
    # all instances, it stops you from making a variable of the (un-parameterized) type Animal and then assign it to a
    # Panda instance (which would violate LSP).
    def eat(self, food: Bamboo) -> None:
        # This check would not be necessary in C++ or Java, but Python ignores types.
        if not isinstance(food, Bamboo):
            raise TypeError("Pandas only eat Bamboo.")
        food.eat()


if __name__ == '__main__':

    print()
    print("Child instance assigned to un-parameterized Parent variable...")
    animal: Animal = Panda()  # Java or C++ would not allow you to declare an un-parameterized Animal
    # animal.execute(Food())  # run-time error and LSP violation
    animal.eat(Bamboo())

    print()
    print("Child instance assigned to parameterized Parent variable...")
    animal: Animal[Bamboo] = Panda()  # Java or C++ would not allow you to declare an un-parameterized Animal
    # animal.execute(Food())  # compile time warning, and run-time error if you run it in Python. Doesn't violate LSP.
    animal.eat(Bamboo())

    print()
    print("Child instance assigned to Child variable...")
    panda1: Panda = Panda()
    panda1.eat(Bamboo())
    # panda1.eat(Food())  # compile-time warning, only produces a run-time error since I explicitly added it

    print()
    print("Parent instance assigned to Child variable...")
    panda2: Panda = Animal()  # compile-time warning, but run succeeds. Would be a compile-time error in Java / C++
    panda2.eat(Bamboo())
    panda2.eat(Food())  # compile-time warning, but run succeeds
