'''
Created on Mar 18, 2014

@author: Mark.E.Frymire
'''

# Tuples are immutable
bigTuple = ("abcd", 786, 2.23, "john", 70.2)
smallTuple = 123, "john"  # the parentheses are optional

print
print "bigTuple:", bigTuple           
print "bigTuple[0]:", bigTuple[0] 
print "bigTuple[1:3]:", bigTuple[1:3]  # excludes element 3 (weird!)
print "bigTuple[2:]:", bigTuple[2:] 
print "bigTuple[-2]:", bigTuple[-2]
print "smallTuple * 2:", smallTuple * 2
print "bigTuple + smallTuple:", bigTuple + smallTuple


# Special cases
emptyTuple = ()
print emptyTuple
single = ("oneElement",) # Use a comma for a tuple with 1 element
print single

# Tuples are immutable
#bigTuple[2] = 1000 # run-time error (why not compile-time?)

# Construct a tuple with a repeated value
hi4 = ("Hi!",) * 4
print hi4

# Convert from a list
tupleFromList = tuple( [3, 1, 2] )
print tupleFromList
print min(tupleFromList)