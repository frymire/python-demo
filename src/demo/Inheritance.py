'''
Created on May 12, 2014

@author: Mark.E.Frymire
'''
class Parent:        # define parent class
    parentAttr = 100
    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print 'Calling parent method'
        
    def myMethod(self):
        print "I'm the parent."

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute:", Parent.parentAttr

class Child(Parent): # define child class
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print 'Calling child method'
        
    def myMethod(self):
        print "I'm the child."
        

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.myMethod()         # call the overridden method.
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


# Python also lets you use multiple inheritance.  It looks like the 
# Parent 2 constructor isn't called, and you just inherit the methods.
class Parent1:
    def __init__(self):
        print "Parent1 constructor"
        
    def dadTalk(self):
        print "I'm the dad."
        
class Parent2:
    def __init__(self):
        print "Parent2 constructor"
        
    def momTalk(self):
        print "I'm the mom."
        
class Child12(Parent1, Parent2):
    def parentsTalk(self):
        self.dadTalk()
        self.momTalk()
        
print
c12 = Child12()
c12.parentsTalk()

# Python provides functions to check subclass and instance relationships.
print
print "issubclass(Child12, Parent1):\t", issubclass(Child12, Parent1)
print "issubclass(Parent1, Child12):\t", issubclass(Parent1, Child12)
print "isinstance(c12, Child12):\t", isinstance(c12, Child12)
print "isinstance(c12, Parent1):\t", isinstance(c12, Parent1)
print "isinstance(c12, Parent2):\t", isinstance(c12, Parent2)
print "isinstance(c12, Parent):\t", isinstance(c12, Parent)

# Overload the + operator with __add__
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print "\n", v1 + v2


# Use a double underscore to hide attributes.  Still, the only protection is that 
# Python changes the value to include the class name, as _JustCounter__secretCount,
# which is pointless and stupid, because you can still change it.
class JustCounter:
    __secretCount = 0 
  
    def count(self):
        self.__secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
# print counter.__secretCount # Error
print counter._JustCounter__secretCount
counter._JustCounter__secretCount += 10 
print counter._JustCounter__secretCount
