'''
Created on Mar 15, 2014

@author: Mark.E.Frymire
'''

# To make a block for an if statement, each line must be indented the same amount.
if (True): 
    print "It's True."
    print "Yep, True."
    print
    
if (False): print "It's False."

# Anything non-zero evaluates to true
if (1): print "1 is true."
if (0): print "0 is true."
if (-1): print "-1 is true."


# Do if-then-else like this
print
if (True):
    print "It's True."
else:
    print "It's False."
    
# Use elif for multiple else statements
print
var = 100
if var == 200:
    print "1 - Got a true expression value"
    print var
elif var == 150:
    print "2 - Got a true expression value"
    print var
elif var == 100:
    print "3 - Got a true expression value"
    print var
else:
    print "4 - Got a false expression value"
    print var
    

# Of course, you can nest if statements
print
var = 100
if var < 200:
    print "Expression value is less than 200"
    if var == 150:
        print "Which is 150"
    elif var == 100:
        print "Which is 100"
    elif var == 50:
        print "Which is 50"
elif var < 50:
    print "Expression value is less than 50"
else:
    print "Could not find true expression"
    

# While-loops can also include an "else"
print
count = 2
while (count < 5):
    print 'The count is:', count
    count = count + 1
else:
    print count, " is not less than 5"
    
# Loop over integers are exclusive of the end term.
print
for i in range(3): print i 
print
for i in range(10,13): print i 

# For-loops can also have else statements
print
for i in range(3):
    print i
else:
    print "No longer in {0, 1, 2}."

    
# Loop over a list
fruits = ['banana', 'apple', 'mango']
print
for fruit in fruits: print 'Current fruit:', fruit
print '\nInt loop over fruits: '
for i in range( len(fruits) ): print 'Current fruit:', fruits[i]


# Break out of and continue in loops like this.

print
for letter in 'Python':
    if letter == 't': continue
    if letter == 'o': break
    print 'Current Letter:', letter

print
var = 7
while var > 0:              
    var -= 1
    if var == 4: continue
    if var == 2: break
    print 'Current variable value:', var
    

# Use pass as a null operation in a loop.  Like a continue, but with the option 
# to add code different from the main code of the loop.  Useful placeholder?
print
for letter in 'Python': 
    if letter == 'h':
        pass
        print 'This is pass block'
    print 'Current Letter :', letter

