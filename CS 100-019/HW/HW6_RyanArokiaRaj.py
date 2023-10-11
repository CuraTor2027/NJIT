'''
    Ryan Arokia-Raj
    20231011
    CS100-019
    HW6_RyanArokiaRaj.py
'''

# 1
def hasFinalLetter(strList, letters):
    strListNew = []
    for i in range(len(strList)):
        for j in range(len(letters)):
            if strList[i][-1] == letters[j]:
                strListNew.append(strList[i])
                break
    return strListNew

strList = ["This", "is", "a", "random", "sentence"]
letters = "stringOfUpperAndLowerCaseLetters"
print(hasFinalLetter(strList, letters))

strList = ["Python", "is", "a", "fun", "language", "to", "learn"]
letters = "pzorjgpoeIJRGFNPIRgnjGRJRSJnGNj"
print(hasFinalLetter(strList, letters))

strList = ["My", "major", "is" "computer" "science"]
letters = "DjfnFDIDjnIJDgnIJfnfgd"
print(hasFinalLetter(strList, letters))

# 2
def isDivisible(maxInt, twoInts):
    numList = []
    for i in range(1, maxInt + 1):
        if i % twoInts[0] == 0 and i % twoInts[1] == 0:
            numList.append(i)
    return numList

maxInt = 30
twoInts = (2, 3)
print(isDivisible(maxInt, twoInts))

maxInt = 50
twoInts = (3, 4)
print(isDivisible(maxInt, twoInts))

maxInt = 20
twoInts = (5, 7)
print(isDivisible(maxInt, twoInts))
