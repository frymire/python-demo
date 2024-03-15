from collections import Counter, namedtuple

# Counter
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(my_list)
print(counter)
print(list(counter.keys()))
print(f"Apples: {counter['apple']}")
print(f"Oranges: {counter['orange']}")
print(f"Grapes: {counter['grape']}")  # 'grape' is not in my_list, so its count will be 0

# namedtuple
Person = namedtuple('Person', ['name', 'age', 'occupation'])
person1 = Person(name='Alice', age=30, occupation='Engineer')
person2 = Person(name='Bob', age=24, occupation='Artist')
print(f"Name: {person1.name}, Age: {person1.age}, Occupation: {person1.occupation}")
print(f"Name: {person2[0]}, Age: {person2[1]}, Occupation: {person2[2]}")
for field in person1:
    print(field)
