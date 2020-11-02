import turtle
import os
import random
counter = 1
ver_pos=0
hor_pos=0





# Setup screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle Test 1")


# Setup pen
turtle.pencolor("white")
turtle.penup()
turtle.shape("turtle")

print ("CURRENT POSITION : ", turtle.pos())

while counter>0:
    #variables take random values
    #random speed
    turtle_speed= random.randint(1, 1)
    #random amount of movement
    move=random.randint(1,200)
    #random degrees to turn
    turn=random.randint(-2,2)
    turn=turn*90

    print ("MOVE : ", move)
    print ("TURN : ", turn)
    

    # turtle movement
    turtle.speed(turtle_speed)
    turtle.right(turn)

   

    # take care that turtle moves within the screen limits
    if turtle.heading() == 0 and hor_pos + move > 300:
        print (hor_pos + move )
        move = 0
        print ("CHANGE OF PLANS. NEW MOVE : ", move)
    elif turtle.heading() == 90 and ver_pos + move > 300:
        print (ver_pos + move)
        move = 0
        print ("CHANGE OF PLANS. NEW MOVE : ", move)
    elif turtle.heading() == 180 and hor_pos - move > -300:
        print (hor_pos - move)
        move = 0
        print ("CHANGE OF PLANS. NEW MOVE : ", move)
    elif turtle.heading() == 270 and ver_pos - move > -300:
        print (ver_pos - move)
        move = 0
        print ("CHANGE OF PLANS. NEW MOVE : ", move)
             
        pass
    turtle.forward(move)
    
    # find turtle angle
    a=turtle.heading()

    # calculate new turtle position
    if (a == 0):
        hor_pos=hor_pos+move
    elif a == 90:
        ver_pos=ver_pos+move
    elif a == 180:
        hor_pos=hor_pos-move
    elif a == 270:
        ver_pos=ver_pos-move
    
    print ("CURRENT POSITION : ", turtle.pos())
    print ("HORISONTAL POSITION : ", hor_pos, "VERTICAL POSITION : ", ver_pos)
    
   
  

    
    





delay = input ("Press enter to exit")
