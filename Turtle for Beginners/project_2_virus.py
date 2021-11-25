import turtle
bob = turtle.Turtle()
bob.color("blue")
bob.speed(30)


for i in range (220):
	bob.forward(i)
	bob.left(i)

turtle.done()
