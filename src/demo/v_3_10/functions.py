# Specify a function with default arguments like this. You can use " -> [return type]"
# to indicate a return type (e.g. to clarify the code or help static analysis tools),
# but it's not required.
def print_me(a_string="Default string.") -> None:
    print(a_string)
    return  # or "return None". Neither are required when returning None.


# Style convention is to put 2 blank lines before and after each function definition.

print_me("Hi.")
print_me(a_string="Hi.")  # You can also specify the parameters by name
print_me()  # Let it use its default argument.  NOTE: doesn't work without the parentheses.


# Parameters are passed by reference.
def change_me(my_list):
    my_list.append('added by change_me()')


a_list = [8, 9, 10]
print("\n", a_list)
change_me(a_list)
print(a_list)


# The original my_list doesn't change when this is called
# since the local variable is assigned to a new reference.
def change_me_2(my_list):
    my_list = [1, 2, 3, 4]  # Assigns a new reference to my_list
    print("my_list inside the function: ", my_list)
    return


# Now you can call change_me_2 function
another_list = [10, 20, 30]
print("\nClient's another_list before the function: ", another_list)
change_me_2(another_list)
print("Client's another_list after the function: ", another_list)


# You can declare the last argument to be of variable length
def print_variable_args(arg_0, *var_tuple):
    print("arg_0:", arg_0, "\nOther args:")
    for var in var_tuple:
        print(var)
    return


print()
print_variable_args(10)  # Calls it with just the required parameter
print()
print_variable_args(70, 60, 50)  # Here, the last two parameters are part of the variable tuple

# Use "lambda" to create short anonymous (supposedly, even though they have a name) functions.
# They can't contain commands (like print) or multiple expressions.
lambda_sum = lambda arg_1, arg_2: arg_1 + arg_2
print("\n5 + 10 =", lambda_sum(5, 10))


# Here's how to return something.
def sum_two_numbers(arg_1, arg_2):
    total = arg_1 + arg_2
    print("Inside sum_two_numbers:", total)
    return total


print()
a_sum = sum_two_numbers(10, 20)
print("Outside the function:", a_sum)

# Anything declared outside of a function is a global variable and can be accessed locally.
# However, local variables with the same name as the globals will hide the global.
global_total = 0


def sum_with_globals(arg_1, arg_2):
    # Accessing global_total as a global variable, while also using it locally (in the next line), produces an error.
    # print("In sum_with_globals, the global variable global_total is:", global_total) # unresolved reference error
    # Setting global_total here treats it as a local variable (hides the global version of global_total)
    global_total = arg_1 + arg_2
    print("In sum_with_globals, global_total is treated as a local variable:", global_total)
    return global_total


print("\nBefore calling sum_with_globals, global_total =", global_total)
global_sum = sum_with_globals(20, 30)
print("Just called sum_with_globals, which returned:", global_sum)
print("Though sum_with_globals set global_total locally, global_total =", global_total)
