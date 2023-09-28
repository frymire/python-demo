
# Define a class. Note that the first comment is a description for the class.
class Employee:
    """Common base class for all employees"""

    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    @staticmethod
    def display_count():
        print(f"Total Employee {Employee.emp_count}")

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    # Typically garbage collection is handled automatically, 
    # but you can override it if you want to do something special.    
    def __del__(self):
        print(f"{self.__class__.__name__} destroyed.")


# Instantiate some employee instances. Note that you don't have to pass anything for the "self" parameter.
zara = Employee("Zara", 2000)
manni = Employee("Manni", 5000)
zara.display_employee()
manni.display_employee()
print(f"# Employees: {Employee.emp_count}")

# You can add, change, or remove attributes without changing the
# class definition, or use global functions to do the same.
zara.age = 7  # Add an 'age' attribute.
print(zara.age)
print(hasattr(zara, 'age'))
zara.age = 8  # Modify 'age' attribute.
print(zara.age)
setattr(zara, 'age', 10)
print(getattr(zara, 'age'))
del zara.age  # Delete 'age' attribute.
# print(emp1.age)  Would give an error.

# Print out the built-in class attributes.
print()
print(id(zara), id(manni))

# As we exit, the destructor for the employee instances will be called.
print("\nDone.")
