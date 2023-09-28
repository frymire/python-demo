'''
Created on May 31, 2014

@author: Mark.E.Frymire
'''

#!/usr/bin/python

# This is the old, low-level thread model.
import thread
import time


# NOTE: This program doesn't work very well, because the print statement 
# isn't synchronized.  It also doesn't terminate.

# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, count)

# Create two threads as follows
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print "Error: unable to start thread"

while 1:
    pass