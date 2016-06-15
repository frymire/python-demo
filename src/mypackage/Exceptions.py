'''
Created on May 7, 2014

@author: mark.e.frymire
'''

# This works fine.
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: can't find file or read data."
else:
    print "Wrote to file successfully."


# Here's how to catch a particular error type.  You can use a tuple group them, if you want.
print
try:
    fh = open("testfile2", "r")
    fh.write("This is my test file for exception handling!!")
except (IOError, ArithmeticError), argument:
    print "Error: can't find file or read data.  Reason:", argument
else:
    print "Wrote to file successfully."


# You can use "except" without an error type to catch any type.
print
try:
    a = 0
    x = 1 / a
except:
    print "Something bad happened."
else:
    print "Successfully divided by", a
finally:
    print "I'm done trying to divide by", a


# To "throw" your own exception, say "raise".

class YouSuckException(BaseException):
    def __init__(self, arg):
        self.args = arg

try:
    print "\nAbout to raise an exception."
    raise YouSuckException("Tony Romo")
except YouSuckException, argument:
    print "You suck:", argument
else:
    print "Made it through without any exceptions."


# Define a function with an assert.
def convertKelvinToFahrenheit(degreesInK):
    assert (degreesInK >= 0), "Colder than absolute zero!"
    return ( (degreesInK-273) * 1.8 ) + 32

# Do something that causes an assert error.
print
print convertKelvinToFahrenheit(273)
print int( convertKelvinToFahrenheit(505.78) )
print convertKelvinToFahrenheit(-5)

