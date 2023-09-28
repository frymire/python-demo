'''
Created on Mar 21, 2014

@author: mark.e.frymire
'''

# Specify a function with default arguments like this
# TODO: Uhh...how do you specify its type?
def printMe(aString = "Default string."):
    print aString
    return
printMe("Hi.")
printMe(aString = "Hi.") # You can also specify the parameters by name
printMe() # Let it use its default argument.  NOTE: doesn't work without the parentheses.


# Parameters are passed by reference.
def changeMe(myList):
    myList.append('added by changeMe()')
    return

aList = [8, 9, 10]
print "\n", aList
changeMe(aList)
print aList


# Confusingly, though, the original myList doesn't change when this is called 
# TODO: Need to understand this better.
def changeMe2(myList):
    myList = [1,2,3,4] # Assigns a new reference to myList
    print "myList inside the function: ", myList
    return

# Now you can call changeme function
anotherList = [10,20,30]
print "\nClient's anotherList before the function: ", anotherList
changeMe2(anotherList)
print "Client's anotherList after the function: ", anotherList


# You can declare the last argument to be of variable length
def printVariableArgs(arg0, *varTuple):
    print "arg0:", arg0, "\nOther args:"
    for var in varTuple:
        print var
    return

print
printVariableArgs(10) # Calls it with just the required parameter
print
printVariableArgs(70, 60, 50) # Here, the last two parameters are part of the variable tuple


# Use "lambda" to create short anonymous (supposedly, even though they have a name) functions.
# They can't contain commands (like print) or multiple expressions.
lambdaSum = lambda arg1, arg2: arg1 + arg2
print "\n5 + 10 =", lambdaSum(5, 10)


# Here's how to return something.
def sumTwoNumbers(arg1, arg2):
    total = arg1 + arg2
    print "Inside sumTwoNumbers:", total
    return total

print
aSum = sumTwoNumbers(10, 20)
print "Outside the function:", aSum  



# Anything declared outside of a function is a global variable, and can be accessed locally.
# However, local variables with the same name as the globals will hide the global.
globalTotal = 0
def sumWithGlobals(arg1, arg2):
    # If you try to access globalTotal as a global variable, while also using it locally (in the next line), you get an error
    # print "In sumWithGlobals, the global variable globalTotal is:", globalTotal # error
    # Setting globalTotal here treats it as a local variable (hides the global version of globalTotal)
    globalTotal = arg1 + arg2 
    print "In sumWithGlobals, globalTotal is treated as a local variable:", globalTotal
    return globalTotal

print "\nBefore calling sumWithGlobals, globalTotal =", globalTotal
globalSum = sumWithGlobals(20,30)
print "Just called sumWithGlobals, which returned:", globalSum
print "Though sumWithGlobals set globalTotal locally, globalTotal =", globalTotal

