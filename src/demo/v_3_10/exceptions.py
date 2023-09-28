
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can't find file or read data.")
else:
    print("Wrote to file successfully.")

# Here's how to catch a particular error type. You can use a tuple to group them if you want.
print()
try:
    fh = open("testfile2", "r")
    fh.write("This is my test file for exception handling!!")
except (IOError, ArithmeticError) as argument:
    print("Error: can't find file or read data.  Reason:", argument)
else:
    print("Wrote to file successfully.")

# You can use "except" without an error type to catch any type.
print()
try:
    a = 0
    x = 1 / a
except Exception:
    print("Something bad happened.")
else:
    print("Successfully divided by", a)
finally:
    print("I'm done trying to divide by", a)


# To "raise" your own exception, use the "raise" statement.
class NotGoodException(Exception):
    def __init__(self, arg):
        self.args = (arg,)


try:
    print("\nAbout to raise an exception.")
    raise NotGoodException("You messed up.")
except NotGoodException as argument:
    print("It looks like...", argument)
else:
    print("Made it through without any exceptions.")


# Define a function with an assert.
def convert_kelvin_to_fahrenheit(degrees_in_k):
    assert degrees_in_k >= 0, "Colder than absolute zero!"
    return ((degrees_in_k - 273) * 1.8) + 32


# Do something that causes an assert error.
print()
print(convert_kelvin_to_fahrenheit(273))
print(int(convert_kelvin_to_fahrenheit(505.78)))
print(convert_kelvin_to_fahrenheit(-5))
