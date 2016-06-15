'''
Created on Mar 19, 2014

@author: Mark.E.Frymire
'''

import time
import calendar

# Python has a built-in 9-tuple for time (0 is Monday for tm_wday)
# Use asctime to format the tuple nicely.
ticks = time.time()
timeTuple = time.localtime(ticks)
print "Ticks since 12:00 am, 1/1/1970:", ticks
print "Time tuple from ticks:", timeTuple
print "Local current time :", time.asctime(timeTuple)
print "Ticks from time tuple", calendar.timegm(timeTuple)

print "\nCPU time (better for measuring performance):", time.clock()

# Sleep for 2 seconds.
print "\nSleeping..."
time.sleep(2)
print "Done sleeping.\n"

# Print a calendar for a given month
print
print calendar.month(timeTuple.tm_year, timeTuple.tm_mon)
print "1996", calendar.isleap(1996)
print "1999", calendar.isleap(1999)
print "2000", calendar.isleap(2000)
print "2100", calendar.isleap(2100)
