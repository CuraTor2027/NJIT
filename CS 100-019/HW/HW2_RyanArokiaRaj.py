'''
    Ryan Arokia-Raj
    20230916
    CS100-019
    HW2_RyanArokiaRaj.py
'''
#1.
grades = ['A', 'B', 'C', 'D', 'C', 'F', 'C', 'F', 'A', 'B']

frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print(frequency)

#2.
dog_breeds = ["collie", "sheepdog", "Chow", "Chihuahua"]

herding_dogs = dog_breeds[:2]
print(herding_dogs)

tiny_dogs = [dog_breeds[-1]]
print(tiny_dogs)

if "Persian" in dog_breeds:
    print(True)
else:
    print(False)
