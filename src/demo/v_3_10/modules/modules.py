
import support
from support import print_hello
support.print_hello("#1")
print_hello("#2")


def increment_money():
    a_local_var = "Hi, I'm a local string."
    print("Locals:", locals())
    print("Globals:", globals())
    # Python assumes any variable assigned a value in a function is local, so you can't do this...
    # money = money + 1
    # We have to first specify that we're using the global version.
    global money
    money = money + 1


money = 2000
print(money)
increment_money()
print(money)


# Use dir to get the names defined by a module
import math
print(dir(math))

# # Test that we can import and use things from subpackages.  sayHi1 and
# # sayHi2 are imported there, so I don't have to do it explicitly here.
# print()
# import v_2_7
# v_2_7.sayHi1()
# v_2_7.sayHi2()
#
# print()
# from v_2_7 import sayHi1, sayHi2
# sayHi1()
# sayHi2()
