import random
import turtle
import colorsys
bob = turtle.Turtle()
bob.speed(0)
turtle.bgcolor("black")
for i in range(100):
	x= random.randint(-300,300)
	y=random.randint(-300,300)
	z= random.randint(10,30)
	bob.color(colorsys.rgb_to_hsv(random.random(),random.random(),random.random()))
	bob.begin_fill()
	bob.circle(z)
	bob.end_fill()
	bob.penup()
	bob.goto(x,y)
	bob.pendown()
	
	
turtle.done()







turtle.done()
