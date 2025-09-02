import calendar
import time
from datetime import datetime

from tzlocal import get_localzone

# Python has a built-in 9-tuple for time (0 is Monday for tm_wday)
ticks = time.time()
timeTuple = time.localtime(ticks)
print("Ticks since 12:00 am, 1/1/1970:", ticks)
print("Time tuple from ticks:", timeTuple)
print("Local current time :", time.asctime(timeTuple))
print("Ticks from time tuple", calendar.timegm(timeTuple))
print("\nCPU time since starting the current process (better for measuring performance):", time.process_time())

# Measure a delta-time using process_time()
start = time.process_time()
for _ in range(30000000):
    pass
stop = time.process_time()
print("\nCPU time since previous call to process_time:", stop - start)

# process_time() doesn't account for time spent in sleep.
start = time.process_time()
print("\nSleeping...")
time.sleep(1)  # sleep for 1 sec
print("Done sleeping.")
print("CPU time since previous call to process_time:", stop - start)

# Print a calendar for a given month
print()
print(calendar.month(timeTuple.tm_year, timeTuple.tm_mon))
print("1996", calendar.isleap(1996))
print("1999", calendar.isleap(1999))
print("2000", calendar.isleap(2000))
print("2100", calendar.isleap(2100))

# Get the local time zone
local_timezone = get_localzone()
local_timezone_abbreviation = datetime.now(local_timezone).tzname()
print(f"\nLocal Timezone: {local_timezone} ({local_timezone_abbreviation})")
