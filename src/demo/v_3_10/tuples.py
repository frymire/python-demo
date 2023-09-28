
# Tuples are immutable
big_tuple = ("abcd", 786, 2.23, "john", 70.2)
small_tuple = 123, "john"  # the parentheses are optional

print()
print("big_tuple:", big_tuple)
print("big_tuple[0]:", big_tuple[0])
print("big_tuple[1:3]:", big_tuple[1:3])  # excludes element 3 (weird!)
print("big_tuple[2:]:", big_tuple[2:])
print("big_tuple[-2]:", big_tuple[-2])  # second element from the end
print("small_tuple * 2:", small_tuple * 2)
print("big_tuple + small_tuple:", big_tuple + small_tuple)

# Special cases
empty_tuple = ()
print(empty_tuple)
single = ("oneElement",)  # use a comma for a tuple with 1 element
print(single)

# Tuples are immutable
# big_tuple[2] = 1000  # This would raise a TypeError because tuples are immutable.

# Construct a tuple with a repeated value
hi4 = ("Hi!",) * 4
print(hi4)

# Convert from a list
tuple_from_list = tuple([3, 1, 2])
print(tuple_from_list)
print(min(tuple_from_list))
