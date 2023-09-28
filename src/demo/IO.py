'''
Created on Apr 1, 2014

@author: mark.e.frymire
'''
import os

# Get some input from stdin
someInput = raw_input("What do you want?: ")
print "I received:", someInput
 
# Get a Python expression from stdin.  (This may be the first interesting 
# thing that Python does, although this can be achieved in Scala, too.)
pythonInput = input("\nEnter a Python list: ")
for x in pythonInput: print x

# Create a file object in read-only format (the default)
aFile1 = open("../../resources/Let's Say Hi.txt")
# aFile1 = open("../../resources/Let's Say Hi.txt", "r") # explicit
print
print aFile1.name, "was opened in", aFile1.mode, "mode."
aFile1.close()

# Open a file for writing.  If it doesn't exist, create it.
aFile2 = open("../../resources/Test.txt", "w")
print aFile2.name, "was opened in", aFile2.mode, "mode."
aFile2.write("Here's a nice line of text.\n")
aFile2.close()

# Reopen the previous file in append mode.
aFile3 = open("../../resources/Test.txt", "a")
print aFile3.name, "was opened in", aFile3.mode, "mode."
aFile3.write("Append me.\n")
aFile3.close()

# Read some bytes.  "r+" is read/write mode.
# Tell us where we are in the file, then use seek to reposition the pointer back at the beginning.
# For the second parameter, use 0 to start from the beginning of the file, 1 to start from the current
# location, and 2 to start from the end of the file.
aFile4 = open("../../resources/Test.txt", "r+")
print aFile4.name, "was opened in", aFile4.mode, "mode."
print "\nRead String is:", aFile4.read(10), "\tCurrent file position:", aFile4.tell()
aFile4.seek(3, 0) 
print "Read String is:", aFile4.read(10), "\tCurrent file position:", aFile4.tell()
aFile4.seek(-4, 1) 
print "Read String is:", aFile4.read(10), "\tCurrent file position:", aFile4.tell()
aFile4.seek(-11, 2) 
print "Read String is:", aFile4.read(7), "\tCurrent file position:", aFile4.tell()
aFile4.close()

# Change to the resouces directory, then remove a file there.  You'll get an error if it doesn't exist.
# Then, rename "Test.txt" to "You Suck.txt"  Here, you can't create "You Suck.txt" if it already exists 
# (hence, the need to delete it beforehand).
print "\nCurrent directory:", os.getcwd()
os.chdir("../../resources")
print "Current directory:", os.getcwd()
os.remove("You Suck.txt") 
os.rename("Test.txt", "You Suck.txt")

# Delete and remake a subdirectory.  Again, you'll get an error if it already exists.
print "Directory Contents:", os.listdir( os.getcwd() )
os.rmdir("A Subdirectory")
print "Directory Contents:", os.listdir( os.getcwd() )
os.mkdir("A Subdirectory")
print "Directory Contents:", os.listdir( os.getcwd() )

