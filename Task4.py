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

outgoing = set()
non_spam = set()

for call in calls:
    outgoing.add(call[0])
    non_spam.add(call[1])

for text in texts:
    non_spam.add(text[0])
    non_spam.add(text[1])

spam = outgoing.difference(non_spam)
spam = sorted(spam)

#Print message:
print("These numbers could be telemarketers: ")
for item in spam:
    print(item)

