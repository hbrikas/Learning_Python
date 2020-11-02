import turtle
import os

# Setup Window
window = turtle.Screen()
window.screensize (500, 500)
window.bgcolor ("green")
window.title("If")

# Setup Turtle
bill = turtle.Turtle()
bill.shape("turtle")
bill.color ("red")
bill.penup()

#define moving step
step = 15

#define moving functions
def move_left():
    x=bill.xcor()
    x -= step
    if x < -280:
        x = -280
    bill.setheading(180)
    bill.setx(x)

def move_right():
    x=bill.xcor()
    x += step
    if x> 280:
        x=280
    bill.setheading(0)
    bill.setx(x)

def move_up():
    y=bill.ycor()
    y += step
    if y > 280:
        y=280
    bill.setheading(90)
    bill.sety(y)

def move_down():
    y=bill.ycor()
    y -= step
    if y < -280:
        y=-280
    bill.setheading(270)
    bill.sety(y)


    




#Keyboard bindings
turtle.listen()
turtle.onkey (bill.pendown, "d")
turtle.onkey (bill.penup, "u")
turtle.onkey (move_left, "Left")
turtle.onkey (move_right, "Right")
turtle.onkey (move_up, "Up")
turtle.onkey (move_down, "Down")






    









delay = input (" Press ENTER to EXIT")