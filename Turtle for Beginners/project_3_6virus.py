import turtle
bob = turtle.Turtle()

bob.speed(30)
bob.penup()
bob.right(90)
bob.forward(200)
bob.left(90)
bob.pendown()


for j in range(2):
	for color in ["red","blue","green"]:
		bob.color(color)
		bob.penup()
		bob.forward(300)
		bob.left(90)
		bob.forward(200)
		bob.pendown()
		for i in range (220):
			bob.forward(i)
			bob.left(i)

turtle.done()
