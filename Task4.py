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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def noDuplicates(Log): # Returns list of unique phone numbers
    phoneDict = {}
    for phoneLog in Log:
        sendNum, rcvNum = phoneLog[0], phoneLog[1]
        if not sendNum in phoneDict.keys():
            phoneDict[sendNum] = sendNum
        if not rcvNum in phoneDict.keys():
            phoneDict[rcvNum] = rcvNum 
    return phoneDict    

def teleMarket(callDict, textDict):
    spamDict = {}
    num140 = 0
    numNotext = 0

    for key in callDict:
        # include numbers that start with 140
        if key.startswith('140'):
            spamDict[key] = key
            num140 += 1

        # include numbers that are not in texts
        elif not key in textDict.keys():
            spamDict[key] = key
            numNotext += 1
    return spamDict

def test():
    callDict = noDuplicates(calls)
    textDict = noDuplicates(texts)
    spamDict = teleMarket(callDict, textDict)

    print("These numbers could be telemarketers: ")
    for key in spamDict:
        print(key)
    
test()