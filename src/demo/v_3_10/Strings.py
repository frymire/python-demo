
hi = "Hello, cruel world."

print(hi)
print(hi[0])
print(hi[2:5])
print(hi[2:])
print(hi * 2)
print(hi + "TEST")

# Here's the printf analog
print()
print("My name is %s. I am %d years old, and I weigh %.1f lbs!" % ('Zara', 21, 350.27))

print('C:\\nowhere')
print('C:/nowhere')

# You can also specify a raw string
print(r'C:\\nowhere')

print('mark frymire'.capitalize())  # Capitalizes the first letter of the string
for name in 'mark frymire'.split():
    print(name.capitalize(), end=' ')
print()
print('mark frymire'.title())  # Capitalizes the first letter of each word
print("WeIrD CaSe.".lower())  # Converts to lowercase
print("WeIrD CaSe.".upper())  # Converts to uppercase
print("WeIrD CaSe.".swapcase())  # Swaps case

print("  trim me  ".strip())  # Removes leading and trailing whitespace

print("na" * 8 + "...BATMAN!!!")
