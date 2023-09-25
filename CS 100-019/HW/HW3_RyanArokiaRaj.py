'''
    Ryan Arokia-Raj
    20230924
    CS100-019
    HW3_RyanArokiaRaj.py
'''
import turtle
import math

#1
scr = turtle.Screen()
point = turtle.Turtle()

#   Equilateral Triangle
point.fd(100)
point.left(120)
point.fd(100)
point.left(120)
point.fd(100)

#   Square
point.fd(100)
point.left(90)
point.fd(100)
point.left(90)
point.fd(100)
point.left(90)
point.fd(100)

#   Pentagon
point.fd(100)
point.left(72)
point.fd(100)
point.left(72)
point.fd(100)
point.left(72)
point.fd(100)
point.left(72)
point.fd(100)

#2
point.circle(50)
point.circle(100)
point.circle(150)
point.circle(200)

#3
print(f"100! = {math.factorial(100)}")
print(f"Log Base 2 of 1,000,000 = {math.log2(1000000)}")
print(f"Greatest Common Divisors(GCD) of 63 and 49 = {math.gcd(63, 49)}")

input()
