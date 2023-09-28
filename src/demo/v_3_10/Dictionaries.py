
# Dictionaries are hash table types. You can even mix the key types, as long as they are all immutable.
# noinspection PyDictCreation
my_dict = {}
my_dict['one'] = "This is one"
my_dict[2] = "This is two"
print(my_dict['one'])
print(my_dict[2])
print("my_dict.get(2, \"None\"):", my_dict.get(2, "None"))  # Get or else
print("my_dict.get(3, \"None\"):", my_dict.get(3, "None"))  # Get or else

# You can declare a dictionary all at once.
tiny_dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tiny_dict)
print(tiny_dict.keys())
print(tiny_dict.values())
print("len(tiny_dict):", len(tiny_dict))
print("Code key in tiny_dict:", 'code' in tiny_dict)
print("Name key in tiny_dict:", 'Name' in tiny_dict)

# You can update and delete existing values
my_dict[2] = "Now this is three."
print(my_dict)
del my_dict["one"]
print(my_dict)

# Be careful, if you add two entries with the same key, the last one overwrites the previous ones.
a_dict = {1: "one", 2: "two", 3: "three", 1: "ONE"}
print(a_dict)

# Merge a second dictionary into this one
a_dict.update(tiny_dict)
print(a_dict)
