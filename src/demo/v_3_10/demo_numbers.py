
from math import ceil, exp, pi, e
from random import choice, shuffle, random, uniform, randrange

# Here's how to exponentiate
print(2**3)

# Division is done with floats by default.
print(7 / 3)

# Do this for integer division.
print(7 // 3)

# You can do [operator]= with all of the operators
a = 7
a += 2
print(a)  # 9
a -= 3
print(a)  # 6
a /= 3
print(a)  # 2.0
a *= 2.5
print(a)  # 5.0
a **= 3  # exponentiate
print(a)  # 125.0

# Do some math.
print("\n|-4.5| = %f" % abs(-4.5))  # Not in math module.
print("Ceiling of -4.5:", ceil(-4.5))
print("exp(1) =", exp(1))

# A couple of constants are also in the math module
print("pi =", pi, "\te =", e)

# Random numbers
print(choice('Python'))  # get a random element of a list
for i in range(10):
    print('Python'[randrange(2, 5)], end=' ') # prints a random character from {t, h, o} (from "python")
print()
myList = [1, 2, 3, 4, 5]
print(myList)
shuffle(myList)  # shuffles the list in place
print(myList)
print()
for i in range(5):
    print(random(), end=' ')  # specifying the end parameter with a space overrides '\n' by default
print()
for i in range(5):
    print(uniform(50, 100), end=' ')
print()
