import re

# Define a regular expression using a raw string, along with a string to search.
regex = r'(.*) are (.*?) .*'
text = "Cats are smarter than dogs."

# Get the matches, starting at the beginning of the text. re.I means be case-insensitive.
matchObj = re.match(regex, text, re.I)

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No matches.")

# Do the same with search, which finds matches anywhere within the text.
searchObj = re.search(regex, text, re.M | re.I)

if searchObj:
    print("\nsearchObj.group():", searchObj.group())
    print("searchObj.group(1):", searchObj.group(1))
    print("searchObj.group(2):", searchObj.group(2))
else:
    print("\nNothing found.")

# Match checks for a match only at the beginning of a string, while
# search checks for a match anywhere in the string.
print()
matchObj = re.match(r'dogs', text, re.M | re.I)
if matchObj:
    print("matchObj.group():", matchObj.group())
else:
    print("No match.")

searchObj = re.search(r'dogs', text, re.M | re.I)
if searchObj:
    print("searchObj.group():", searchObj.group())
else:
    print("Nothing found.")

# Search and replace.
phone = "2004-959-559 # This is a phone number"
replacement = ""

# Delete Python-style comments
num = re.sub(r'#.*$', replacement, phone)
print("\nPhone Num:", num)

# Remove anything other than digits
num = re.sub(r'\D', replacement, phone)
print("Phone Num:", num)
