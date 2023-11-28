'''
    Ryan Arokia-Raj
    20231127
    CS100-019
    HW11_RyanArokiaRaj.py
'''

class Dog:
    '''Create object Dog with a name and breed'''
    
    def __init__(self, name, breed, tricks, teach):
        self.name = name
        self.breed = breed
        self.tricks = tricks
        self.teach = teach

    def name(self):
        return self.name

    def breed(self):
        return self.breed
    
    def teach(self):
        return self.teach
    
sugar = Dog("Sugar", "Border Collie", [], "frisbee")

# 1.
print(sugar.name)
print(sugar.breed)

# 2.
print(f"\n{sugar.tricks}")

# 3.
print(f"\nSugar knows {sugar.teach}")
