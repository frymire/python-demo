'''
Created on Mar 14, 2014

@author: Mark.E.Frymire
'''

# Dictionaries are hash table types.  You can even mix the key types, as long as they are all immutable.
myDict = {}
myDict['one'] = "This is one"
myDict[2]     = "This is two"
print myDict['one'] 
print myDict[2]
print "myDict.get(2, \"None\"):", myDict.get(2, "None") # Get or else
print "myDict.get(3, \"None\"):", myDict.get(3, "None") # Get or else

# You can declare a dictionary all at once.
tinyDict = {'name': 'john','code': 6734, 'dept': 'sales'}
print tinyDict  
print tinyDict.keys()
print tinyDict.values()
print "len(tinyDict):", len(tinyDict)
print "tinyDict.has_key(\"code\"):", tinyDict.has_key("code")
print "tinyDict.has_key(\"Name\"):", tinyDict.has_key("Name")

# You can update and delete existing values
myDict[2] = "Now this is three."
print myDict
del myDict["one"]
print myDict

# Be careful, if you add two entries with the same key, the last one overwrites the previous ones.
aDict = { 1: "one", 2: "two", 3: "three", 1: "ONE"}
print aDict

# Merge a second dictionary into this one
aDict.update(tinyDict)
print aDict