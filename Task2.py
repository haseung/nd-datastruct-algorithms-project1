"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def maxDuration(callNumbers):  
    maxValue = 0
    for key in callNumbers:
        if callNumbers[key] > maxValue:
            maxValue = callNumbers[key]
            maxNum = key
    return maxNum

# Create empty dictionary for phone numbers
callNumbers = {}

# Populate dictionary for calls
for phoneLog in calls:
    callNum, rcvNum, startTime, duration = phoneLog[0], phoneLog[1], phoneLog[2], int(phoneLog[3])
    if not callNum in callNumbers.keys():
        callNumbers[callNum] = 0
    if not rcvNum in callNumbers.keys():
        callNumbers[rcvNum] = 0

    # Add call durations
    if callNum in callNumbers.keys():
        callNumbers[callNum] += duration
    if rcvNum in callNumbers.keys():
        callNumbers[rcvNum] += duration 

# Identify max duration call
maxNum = maxDuration(callNumbers)

# Print Message
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(maxNum, callNumbers[maxNum]))




