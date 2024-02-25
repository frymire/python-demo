
import json

sample_array = [
    {"name": "John Doe", "age": 30, "is_student": False, "courses": ["Mathematics", "Science"]},
    {"name": "Jane Smith", "age": 25, "is_student": True, "courses": ["Art", "History"]},
    {"name": "Bob Brown", "age": 20, "is_student": True, "courses": ["Biology", "Chemistry"]}
]

file_path = 'sample_array.json'
with open(file_path, 'w') as file:
    json.dump(sample_array, file, indent=4)  # Use indent for pretty printing

with open(file_path, 'r') as file:
    read_array = json.load(file)

for item in read_array:
    print(item)
