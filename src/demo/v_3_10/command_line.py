
# Run this as: python command_line_args_demo.py arg1 arg2 arg3

import sys

# Print the list of command line arguments
print("Command line arguments:", sys.argv)

# Check the number of arguments (excluding the script name)
num_args = len(sys.argv) - 1
print("Number of arguments (excluding script name):", num_args)

# Access individual command line arguments
if num_args >= 1:
    arg1 = sys.argv[1]
    print("Argument 1:", arg1)

if num_args >= 2:
    arg2 = sys.argv[2]
    print("Argument 2:", arg2)

# You can continue accessing more arguments in a similar manner
