
class Parent:

    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parent_method(self):
        print('Calling parent method')

    def my_method(self):
        print("I'm the parent.")

    def set_attr(self, attr):
        Parent.parentAttr = attr

    def get_attr(self):
        print("Parent attribute:", Parent.parentAttr)


# Define Child to inherit from Parent
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')

    def my_method(self):
        print("I'm the child.")


c = Child()
c.childMethod()
c.parent_method()
c.my_method()
c.set_attr(200)
c.get_attr()


class Parent1:

    def __init__(self):
        print("Parent1 constructor")

    def dad_talk(self):
        print("I'm the dad.")


class Parent2:

    def __init__(self):
        print("Parent2 constructor")

    def mom_talk(self):
        print("I'm the mom.")


# Python supports multiple inheritance like this.
class Child12(Parent1, Parent2):
    def parents_talk(self):
        self.dad_talk()
        self.mom_talk()


c12 = Child12()
c12.parents_talk()

print()
print("issubclass(Child12, Parent1):", issubclass(Child12, Parent1))
print("issubclass(Parent1, Child12):", issubclass(Parent1, Child12))
print("isinstance(c12, Child12):", isinstance(c12, Child12))
print("isinstance(c12, Parent1):", isinstance(c12, Parent1))
print("isinstance(c12, Parent2):", isinstance(c12, Parent2))
print("isinstance(c12, Parent):", isinstance(c12, Parent))


class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Vector ({self.a}, {self.b})'

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print()
print(v1 + v2)


class Counter:
    _weakly_secret_count = 0
    __secret_count = 0

    def count(self):
        self._weakly_secret_count += 1
        self.__secret_count += 1


# Accessing variables leading with '_' is discouraged, but allowed.
# Python mangles the names of variables starting with '__', so you can't (easily) access them.
counter = Counter()
counter.count()
counter.count()
print(f"Weakly secret count = {counter._weakly_secret_count}")
# print(counter.__secretCount)  # Error
