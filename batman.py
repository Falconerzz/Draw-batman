import turtle

#initialize method
bat = turtle.Turtle()

#size of pointer and pen
bat.turtlesize(1, 1, 1)
bat.pensize(3)

#screen info
wn = turtle.Screen()
wn.bgcolor("dark blue")
wn.title("BATMAN")

#color
bat.color("yellow", "black")


#begin filling color
bat.begin_fill()

#turn1
bat.left(90)         #turn pointer direction to left of 90
bat.circle(50, 85)   #draw circle of radius
bat.circle(15, 110)
bat.right(180)

#turn2
bat.circle(30, 150)
bat.right(5)
bat.forward(10)      #draw forward line of 10

#turn3
bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)

#turn4
bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

#turn5
bat.forward(30)
bat.left(55)
bat.forward(10)

#reverse

#turn5
bat.forward(10)
bat.left(55)
bat.forward(30)

#turn4
bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)

#turn3
bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)

#turn2
bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)

#turn1
bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)

#end color filling
bat.end_fill()


#end the turtle method
turtle.done()