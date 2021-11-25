import turtle
import math
import random
b=turtle.Turtle()
b.color("red","green")
b.speed(5000)

for i in range (200):
	b.forward(math.sqrt(i*20)*4)
	b.left(150)
	b.right(10)
	
b.ht()
	
turtle.done()
