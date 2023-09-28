import os

# Get some input from stdin
some_input = input("What do you want?: ")
print("I received:", some_input)

# Get a Python expression from stdin.
python_input = input("\nEnter a Python list: ")
for x in python_input:
    print(x)

# Create a file object in read-only format (the default)
a_file1 = open("../../../resources/Let's Say Hi.txt")
# a_file1 = open("../../../resources/Let's Say Hi.txt", "r") # explicit
print()
print(a_file1.name, "was opened in", a_file1.mode, "mode.")
a_file1.close()

# Open a file for writing.  If it doesn't exist, create it.
a_file2 = open("../../../resources/Test.txt", "w")
print(a_file2.name, "was opened in", a_file2.mode, "mode.")
a_file2.write("Here's a nice line of text.\n")
a_file2.close()

# Reopen the previous file in append mode.
a_file3 = open("../../../resources/Test.txt", "a")
print(a_file3.name, "was opened in", a_file3.mode, "mode.")
a_file3.write("Append me.\n")
a_file3.close()

# Read some bytes.  "rb+" is read/write mode in binary.
# Tell us where we are in the file, then use seek to reposition the pointer back at the beginning.
# For the second parameter, use 0 to start from the beginning of the file, 1 to start from the current
# location, and 2 to start from the end of the file.
a_file4 = open("../../../resources/Test.txt", "rb+")
print(a_file4.name, "was opened in", a_file4.mode, "mode.")
print("\nRead String is:", a_file4.read(10), "\tCurrent file position:", a_file4.tell())
a_file4.seek(3, 0)
print("Read String is:", a_file4.read(10), "\tCurrent file position:", a_file4.tell())
a_file4.seek(-4, 1)
print("Read String is:", a_file4.read(10), "\tCurrent file position:", a_file4.tell())
a_file4.seek(-11, 2)
print("Read String is:", a_file4.read(7), "\tCurrent file position:", a_file4.tell())
a_file4.close()

# Change to the resources directory, then remove a file there.  You'll get an error if it doesn't exist.
# Then, rename "Test.txt" to "You Suck.txt"  Here, you can't create "You Suck.txt" if it already exists
# (hence, the need to delete it beforehand).
print("\nCurrent directory:", os.getcwd())
os.chdir("../../../resources")
print("Current directory:", os.getcwd())
os.remove("You Suck.txt")
os.rename("Test.txt", "Renamed test.txt")

# Delete and remake a subdirectory.  Again, you'll get an error if it already exists.
print("Directory Contents:", os.listdir(os.getcwd()))
os.mkdir("A Subdirectory")
print("Directory Contents:", os.listdir(os.getcwd()))
os.rmdir("A Subdirectory")
print("Directory Contents:", os.listdir(os.getcwd()))
