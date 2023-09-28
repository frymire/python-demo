'''
Created on Mar 27, 2014

@author: Mark.E.Frymire
'''
import Support
Support.print_func("#1")
    
from Support import print_func
print_func("#2")


Money = 2000
print Money

def incrementMoney():
    aLocalVar = "Hi, I'm a local string."
    print "Locals:", locals()
    print "Globals:", globals()    
    # Python assumes any variable assigned a value in a function is local, so you can't do this...
    # Money = Money + 1
    # We have to first specify that we're using the global version.
    global Money    
    Money = Money + 1

incrementMoney()
print Money


# Use dir to get the names defined by a module
import math
print dir(math)

# Test that we can import and use things from subpackages.  sayHi1 and  
# sayHi2 are imported there, so I don't have to do it explicitly here.
print
import v_2_7
v_2_7.sayHi1()
v_2_7.sayHi2()
   
print
from v_2_7 import sayHi1, sayHi2
sayHi1()
sayHi2()