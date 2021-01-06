"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def test():
    print("Total Text Numbers: ", len(textNumbers))
    print("Total Call Numbers: ", len(callNumbers))
    print("Total Phone Numbers: ", len(phoneNumbers))

# create dictionary for phone numbers
textNumbers = {}
callNumbers = {}
phoneNumbers ={}

# Populate dictionary for texts
for item in texts:
    textNumbers[item[0]] = 0
    textNumbers[item[1]] = 0

# Population dictionary for calls
for item in calls:
    callNumbers[item[0]] = 0
    callNumbers[item[1]] = 0

# Update phone list to identify unique numbers
phoneNumbers.update(textNumbers)
phoneNumbers.update(callNumbers)

# Print message
print("There are {0} different telephone numbers in the records.".format(len(phoneNumbers)))


