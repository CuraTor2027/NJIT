'''
    Ryan Arokia-Raj
    20230926
    CS100-019
    HW4_RyanArokiaRaj.py
'''
import turtle

a = 3
b = 4
c = 5

# 1, 2
if a < b:
    print("OK")
else:
    print("NOT OK")

if c < b:
    print("OK")
else:
    print("NOT OK")

if (a + b) == c:
    print("OK")
else:
    print("NOT OK")

if ((a**2) + (b**2)) == (c**2):
    print("OK")
else:
    print("NOT OK")

# 3
scr = turtle.Screen()
cursor = turtle.Turtle()

color = input("Enter a color: ")
lineWidth = int(input("Enter a line width: "))
lineLength = int(input("Enter a line length: "))
shape = input("Enter a shape(line, triangle or square): ")

cursor.color(color)
cursor.width(lineWidth)

if shape == "line":
    cursor.fd(lineLength)
elif shape == "triangle":
    cursor.fd(lineLength)
    cursor.left(120)
    cursor.fd(lineLength)
    cursor.left(120)
    cursor.fd(lineLength)
elif shape == "square":
    cursor.fd(lineLength)
    cursor.left(90)
    cursor.fd(lineLength)
    cursor.left(90)
    cursor.fd(lineLength)
    cursor.left(90)
    cursor.fd(lineLength)

input()
