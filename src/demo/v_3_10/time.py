from time import time  # type: ignore
from datetime import datetime

seconds_since_epoch = time()
print("Seconds since Unix epoch:", seconds_since_epoch)

current_datetime = datetime.fromtimestamp(seconds_since_epoch)

local_time_zone = datetime.now().astimezone().tzinfo
print(f"Local Time ({local_time_zone}):", current_datetime.strftime('%Y-%m-%d %H:%M:%S'))
print(f"Local Time ({local_time_zone}):", current_datetime.strftime('%-d %B %Y, %I:%M:%S %p'))
formatted = current_datetime.strftime('%B %-d, %Y, %I:%M:%S.%f')[:-3] + ' ' + current_datetime.strftime('%p')
print(f"Local Time ({local_time_zone}):", formatted)

current_datetime_utc = datetime.utcfromtimestamp(seconds_since_epoch)
print("Time (UTC):", current_datetime_utc.strftime('%Y-%m-%d %H:%M:%S'))
