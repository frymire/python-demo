'''
Created on Mar 14, 2014

@author: Mark.E.Frymire
'''

from string import capitalize, strip

hi = "Hello, cruel world."

print hi
print hi[0]
print hi[2:5]
print hi[2:]
print hi * 2
print hi + "TEST"

# Here's the printf analog
print
print "My name is %s. I am %d years old, and I weigh %.1f lbs!" % ('Zara', 21, 350.27) 

print 'C:\\nowhere'
print 'C:/nowhere'

# You can also specify a raw string
print r'C:\\nowhere'

print capitalize('mark frymire') # Doesn't capitalize the last name
for name in 'mark frymire'.split(): print capitalize(name),
print
print 'mark frymire'.title()
print "WeIrD CaSe.".lower()
print "WeIrD CaSe.".upper()
print "WeIrD CaSe.".swapcase()


print strip("  trim me  ")

print "na"*8 + "...BATMAN!!!"