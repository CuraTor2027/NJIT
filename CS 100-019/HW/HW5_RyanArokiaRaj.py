'''
    Ryan Arokia-Raj
    20230926
    CS100-019
    HW4_RyanArokiaRaj.py
'''

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# 1
for i in range(len(months)):
    if months[i][0] == "J":
        print(months[i])

# 2
for i in range(100):
    if i % 2 == 0 and i % 5 == 0:
        print(i)

# 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for i in range(len(horton)):
    for j in range(len(vowels)):
        if horton[i] == vowels[j]:
            print(horton[i], end = " ")
