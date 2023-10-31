'''
    Ryan Arokia-Raj
    20231011
    CS100-019
    HW8_RyanArokiaRaj.py
'''

def twoWords(length, firstLetter):
    while True:
        word_one = input(f"Enter a {letter}-letter word please: ")
        if len(word_one) != letter:
            continue
        else:
            break
    while True:
        word_two = input(f"Enter a word beginning with {firstLetter} please: ")
        if word_two[0].upper() != str(firstLetter):
            continue
        else:
            break

    list1 = []
    list1.append(word_one)
    list1.append(word_two)
    return list1

letter = 4
firstLetter = 'B'
print(twoWords(letter, firstLetter))
