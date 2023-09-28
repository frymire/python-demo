
big_list = ['abcd', 786, 2.23, 'john', 70.2]
small_list = [123, 'john']

print("big_list:", big_list)
print('len(big_list)', len(big_list))
print("big_list[0]", big_list[0])
print("big_list[1:3]:", big_list[1:3])  # excludes element 3 (weird!)
print("big_list[2:]:", big_list[2:])
print("big_list[-2] (index from the right):", big_list[-2])
print("small_list * 2:", small_list * 2)
print("big_list + small_list:", big_list + small_list)

# Check list membership
print("786 in big_list:", 786 in big_list)
print("786 in small_list:", 786 in small_list)
print("786 not in big_list:", 786 not in big_list)

# Update a list element
big_list[2] = 1000  # okay for lists, not okay for tuples which are immutable
print()
print("After big_list[2] = 1000:", big_list)
del big_list[2]
print("After delete big_list[2]:", big_list)
big_list.append("AppendMe")
print("After append:", big_list)

print("Max:", max([20, 5, 50, 10]))
print("Sorted:", sorted([20, 5, 50, 10]))  # sorting doesn't affect the original list
big_list.reverse()  # reversing does affect the original list
print("After reverse:", big_list)
last = big_list.pop()
print("After pop:", big_list, "\tPopped element:", last)
big_list.insert(2, "InsertMe")
print("After insert:", big_list)
big_list.remove("InsertMe")
print("After remove:", big_list)
print("Index of john:", big_list.index("john"))

# Construct a list with a repeated value
hi4 = ["Hi!"] * 4
print(hi4)
