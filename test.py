myDict = {'a':1, 'b':2, 'c':1, 'd':4}
maxVal = max(myDict, key = lambda k: myDict[k])
print(maxVal)