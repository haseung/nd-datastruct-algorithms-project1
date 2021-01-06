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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# convert date str of month, day, year, time into list of integers
def date2int(date):
    date = date.split(' ')
    timeOnly = date[1].split(':')
    dateOnly = date[0].split('-')

    hours, minutes, seconds = int(timeOnly[0]), int(timeOnly[1]), int(timeOnly[2])
    day = int(dateOnly[0])
       
    return day, hours, minutes, seconds 

def dateIsBefore(startDate, nextDate):
    day1, hours1, minutes1, seconds1 = startDate[0], startDate[1], startDate[2], startDate[3]
    day2, hours2, minutes2, seconds2 = nextDate[0], nextDate[1], nextDate[2], nextDate[3]
    if day1 < day2:
        return True
    elif day1 == day2:
        if hours1 < hours2:
            return True
        elif hours1 == hours2:
            if minutes1 < minutes2:
                return True
            elif minutes1 == minutes2:
                return seconds1 < seconds2
    return False  

def test():
    assert date2int("1-9-2016 6:03:22") == (1, 6, 3, 22)
    assert dateIsBefore([1, 6, 3, 22], [1, 6, 3, 22]) == False 
    assert dateIsBefore([1, 6, 3, 22], [1, 6, 3, 23]) == True
    assert dateIsBefore([1, 6, 3, 22], [1, 6, 3, 21]) == False

# Check for first record of texts
firstText = texts[0] 
for item in texts:
    firstTextDate = date2int(firstText[2])
    nextTextDate = date2int(item[2])
    if not dateIsBefore(firstTextDate, nextTextDate):
        firstText = item

# Check for last record of calls
lastCall = calls[0]
for item in calls:
    lastCallDate = date2int(lastCall[2])
    nextCallDate = date2int(item[2])
    if dateIsBefore(lastCallDate, nextCallDate):
        lastCall = item

# Print messages:
print("First record of texts, {0} texts {1} at time {2}".format(firstText[0],firstText[1],firstText[2]))
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(lastCall[0],lastCall[1],lastCall[2],lastCall[3]))


