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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def callbyArea(areaCode): # Returns list of calls by area code
  areaList = []
  for item in calls:
    if item[0].startswith(areaCode):
      areaList.append(item)  
  numCalls = len(areaList) 
  return areaList, numCalls

def noMarketers(areaList, areaCode): # Removes telemarketers and identifies fixed line received calls
  recvList = []
  numFixed = 0
  for item in areaList:
    if not item[1].startswith('140'): # check for non-telemarketer calls
      recvList.append(item[1])
      if item[1].startswith(areaCode): # check if receiver is fixed line
        numFixed += 1  
  return recvList, numFixed # Returns list of only receive calls & number of calls to fixed lines

def codeList(recvList): # Returns a list of phone codes only
  codesList = []
  for item in recvList:
    if item.startswith('('): # fixed lines
      item = item.split(')').pop(0) + ')'
      codesList.append(item)
    elif item.startswith('7') or item.startswith('8') or item.startswith('9'): # mobile lines
      item = item[0:4]
      codesList.append(item)
  return codesList

def noDoubles(codesList):  # Remove duplicate numbers
  noDoubles = {}  
  unsortList = []
  
  for item in codesList: # populates a dictionary to remove doubles from codeList
    if not item in noDoubles.keys():
      noDoubles[item] = item
  
  for key in noDoubles: # converts dictionary back to list
    unsortList.append(noDoubles.get(key))
  return unsortList

def test():

  # 1. Create list of calls from (080)
  areaCode = '(080)'
  areaList, numCalls = callbyArea(areaCode)

  # 2. Create list of received calls without telemarketers and to fixed numbers
  recvList, numFixed = noMarketers(areaList, areaCode)

  # 3. Create a list of only codes
  codesList = codeList(recvList)
  
  # 4. Remove duplicates
  codesList = noDoubles(codesList)

  # 5. Sort final list lexigraphically
  codesList.sort()

  # Solution
  # Part A
  print("The numbers called by people in Bangalore have codes:")
  for item in codesList:
    print(item)

  # Part B 
  print('{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(numFixed / numCalls))

test()  
