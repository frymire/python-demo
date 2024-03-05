import json
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

print("\nTo JSON and back...")
json_format = '%Y-%m-%d %H:%M:%S.%f'
json_datetime = json.dumps({"time": current_datetime.strftime(json_format)})
print("JSON:", json_datetime)

parsed_json_string = json.loads(json_datetime)["time"]
parsed_datetime = datetime.strptime(parsed_json_string, '%Y-%m-%d %H:%M:%S.%f')
print("Time (UTC):", parsed_datetime.strftime('%Y-%m-%d %H:%M:%S'))
parsed_formatted = parsed_datetime.strftime('%B %-d, %Y, %I:%M:%S.%f')[:-3] + ' ' + parsed_datetime.strftime('%p')
print(f"Local Time ({local_time_zone}):", parsed_formatted)
