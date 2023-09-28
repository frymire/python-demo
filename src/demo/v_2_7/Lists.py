'''
Created on Mar 14, 2014

@author: Mark.E.Frymire
'''

bigList = ['abcd', 786, 2.23, 'john', 70.2]
smallList = [123, 'john']

print "bigList:", bigList
print 'len(bigList)', len(bigList)
print "bigList[0]", bigList[0]
print "bigList[1:3]:", bigList[1:3] # excludes element 3 (weird!)
print "bigList[2:]:", bigList[2:]
print "bigList[-2] (index from the right):", bigList[-2]
print "smallList * 2:", smallList * 2
print "bigList + smallList:", bigList + smallList

# Check list membership
print "786 in bigList:", 786 in bigList
print "786 in smallList:", 786 in smallList
print "786 not in bigList:", 786 not in bigList

# Update a list element
bigList[2] = 1000
print
print "After bigList[2] = 1000:", bigList
del bigList[2]
print "After delete bigList[2]:", bigList
bigList.append("AppendMe")
print "After append:", bigList

print "Max:", max( [20, 5, 50, 10] )
print "Sorted:", #??? Couldn't get this to work.
bigList.reverse()
print "After reverse:", bigList
last = bigList.pop()
print "After pop:", bigList, "\tPopped element:", last
bigList.insert(2, "InsertMe")
print "After insert:", bigList
bigList.remove("InsertMe")
print "After remove:", bigList
print "Index of john:", bigList.index("john")

# Construct a list with a repeated value
hi4 = ["Hi!"] * 4
print hi4
