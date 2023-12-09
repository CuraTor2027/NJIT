'''
    Ryan Arokia-Raj
    20231208
    CS100-019
    HW12_RyanArokiaRaj.py
'''

def safeOpen(filename):
    try:
        inputFile = open(filename)
        print(inputFile)
    except:
        print("None")

def safeOpen_2(filename):
    try:
        inputFile = open(filename)
        return inputFile
    except:
        print("File not found. Please try again.")

def safeOpen_3(filename):
    try:
        inputFile = open(filename)
        return inputFile
    except:
        print("File not found. Yet another human error. Goodbye.")

def safeFloat(x):
    try:
        float(x)
    except:
        print(0.0)

def averageSpeed():
    for i in range(1):
        filename = input("Enter file name: ")
        if i == 0:
            inputFile = safeOpen_2(filename)
        elif i == 1:
            inputFile = safeOpen_3(filename)
    content = inputFile.readlines()
    sum = 0
    count = 0
    for line in content:
        for i in line:
            if i.isdigit() == True:         
                sum += float(i)
                count += 1
    average = sum / count
    print(f"Average speed is {average} miles per hour.")

# 1.
filename = "ghost.txt"
safeOpen(filename)

# 2.
safeFloat("abc")

# 3.
averageSpeed()
