
# Say hello.
print("Hello, python noob.")

# Split strings over multiple lines, no need for +.
print(
    "Please go embarrass yourself "
    "someplace else."
)

# Print multiple things on one line. Python automatically adds a space between them.
print("Hello,", "world.")

# Read a character from stdin
c = input("Type 'a': ")
if c == 'a':
    print(c)
elif c == 'b':
    print("Wrong!")
else:
    print("[Sigh...] Not even close.")

# To print without a newline, use write() from the sys module.
import sys
x = 'foo'
sys.stdout.write(x)
sys.stdout.write(" hi")
print()

# You can assign multiple variables at once.
ten, mole, me = 10, 6.02e+23, "Mark Frymire"
print(ten)
print(mole / 6.02)
print(me)

# Python uses float division by default
print(3/5) # 0.6
print(3//5) # integer division, returns 0

# You can also assign multiple variables to a common value
a = b = c = 1
print(a)
print(b)
print(c)

# Boolean comparators
print(True and False)
print(True and True)
print(True or False)
print(False or False)
print(not True)  # use "not" instead of !
print(not False)


# Number types in python are immutable. Example...
print()
a = 20
b = 20

# Since integers in Python are immutable, Python caches small integers to improve performance.
# In this case, both a and b are assigned the same integer value, which is within the range of
# cached small integers, so they refer to the same object.
print(a is b) # True
print(id(a) == id(b)) # True, since a and b refer to the same object

# Now update b...
b = 30
print(a is b) # False, b now points to a different immutable int instance
print(a is not b) # True, same reason
