'''
    Ryan Arokia-Raj
    20231118
    CS100-019
    HW10_RyanArokiaRaj.py
'''

def initialLetterCount(wordList):
    wordList_dict = {}

    initialLetters = []
    list_keys = []
    list_values = []

    for i in range(len(wordList)):
        initialLetters.append(wordList[i][0])

    for i in initialLetters:
        if str(initialLetters[i]) in list_keys == False:
            list_keys.append(initialLetters[i])
    print(list_keys)
    return wordList_dict



# 1.
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))
