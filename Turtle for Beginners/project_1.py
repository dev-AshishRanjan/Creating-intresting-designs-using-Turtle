import turtle
bob= turtle.Turtle()

bob.speed(100)

bob.color("red","cyan")
bob.begin_fill()
for i in range (36):
	bob.forward(300)
	bob.left(170)
	
bob.end_fill()

bob.penup()
bob.backward(200)
bob.right(90)
bob.forward(200)
bob.pendown()

bob.color("blue","green")
bob.begin_fill()
for j in range (72):
	bob.forward(200)
	bob.left(175)
bob.end_fill()

bob.penup()
bob.backward(400)
bob.pendown()

bob.color("orange","yellow")
bob.begin_fill()
for i in range(100):
	bob.forward(200)
	bob.right(185)
bob.end_fill()
	
turtle.done()
