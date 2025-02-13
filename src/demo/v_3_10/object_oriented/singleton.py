from typing import Optional


class Singleton:

    singleton: Optional['Singleton'] = None

    def __new__(cls) -> 'Singleton':
        if cls.singleton is None:
            print("Instantiating.")
            cls.singleton = super().__new__(cls)
        else:
            print("Reusing.")
        return cls.singleton


if __name__ == "__main__":
    s1 = Singleton()  # Instantiating.
    s2 = Singleton()  # Reusing.
    print(s1 is s2)
