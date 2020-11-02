import turtle
import os

a=10
b=2
print ("a = ", a, "b = ", b)
print ("press a for + ", "press b for - ", "press c for * ", "press d for /")

def add():
    result=a+b

def sub():
    result = a - b

def mult():
    result = a * b

def dev():
    result = a / b

turtle.onkey(add, "a")
turtle.onkey (sub, "b")


delay = input (" Press ENTER to EXIT")