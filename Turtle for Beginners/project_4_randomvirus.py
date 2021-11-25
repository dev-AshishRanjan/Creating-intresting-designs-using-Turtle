import turtle
import random

bob = turtle.Turtle()

bob.speed(50)

l=["cyan","green","yellow"]

for j in range(10):
	for color in ["red","blue","green"]  :
		bob.color(color )
		bob.penup()
		bob.forward(300)
		bob.left(90)
		bob.forward(200)
		bob.pendown()
		for i in range (random.randint(200,250)):
			
			bob.forward(i)
			bob.left(i)

turtle.done()
