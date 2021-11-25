#Courtesy : https://docs.python.org/3/library/turtle.html
import turtle
b= turtle.Turtle()
b.color("red","yellow")
b.begin_fill()
while True:
	b.forward(200)
	b.left(170)
	if abs(b.pos())<1:
		break
		
b.end_fill()
turtle.done()
