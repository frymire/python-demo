'''
Created on Mar 6, 2013

@author: mark.e.frymire
'''

# This is just a comment.
print "You suck."  # Here's another comment.

print "You're embarrassing " \
    "yourself."
    
# Print multiple things on one line.  Python automatically adds a space between them.
print "Hello,", "world."

# c = raw_input ("Type 'a': ")
#  
# if (c == 'a'):
#     print c
# elif (c == 'b'):
#     print "Wrong!"
# else:
#     print "Not even close, idiot."

print """Please go suck
  someplace else."""

# To print without a newline, use write() from the sys module.
import sys
x = 'foo'
sys.stdout.write(x)
sys.stdout.write(" hi")
print

# You can assign multiple variables at once.  Note that number types are immutable
ten, mole, me = 10, 6.02e+23, "Mark Frymire"
print ten
print (mole/6.02)
print me

# You can also assign multiple variables to a common value
a = b = c = 1
print a
print b 
print c 


# Boolean comparators
print (True and False)
print (True and True)
print (True or False)
print (False or False)
print not(True)  # use "not" instead of !
print not(False)

# These don't make sense.  They're supposed to be comparing memory locations (?)
print
a = 20
b = 20
print ( a is b )
print ( id(a) == id(b) )

b = 30
print ( a is b )
print ( a is not b )
