class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


dog = Dog()
cat = Cat()
cow = Cow()

print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
print(cow.speak())  # Moo!
