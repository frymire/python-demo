'''
Created on May 8, 2014

@author: mark.e.frymire
'''

# Define a class.  Note that the first comment is a description for the class.
class Employee:
    'Common base class for all employees'
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
        
    def displayEmployee(self):
        print "Name: %s, Salary: %d" % (self.name, self.salary)
    
    # Typically garbage collection is handled automatically, 
    # but you can override it, if you want to do something special.    
    def __del__(self):
        print self.__class__.__name__, "destroyed."
    
      
      
# Instantiate some employee instances.  Note that you don't have to pass anything for the "self" parameter.
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "# Employees: %d" % Employee.empCount

# You can add, change, or remove attributes without changing the class definition, or
# use global functions to do the same, both of which seem stupid.
emp1.age = 7  # Add an 'age' attribute.
print emp1.age
print hasattr(emp1, 'age')
emp1.age = 8  # Modify 'age' attribute.
print emp1.age
setattr(emp1, 'age', 10)
print getattr(emp1, 'age')
del emp1.age  # Delete 'age' attribute.
# print emp1.age  Would give an error.

# Print out the built-in class attributes.
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__   # module where the class is defined
print "Employee.__bases__:", Employee.__bases__     # a tuple containing base classes
print "Employee.__dict__:", Employee.__dict__       # the class's namespace

# We can get explicit IDs for each instance.
print
print id(emp1), id(emp2)

# As we exit, the destructor for the employee instances will be called.
print "\nDone."


