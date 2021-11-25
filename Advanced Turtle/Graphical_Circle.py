import turtle
bob= turtle.Turtle()
bob.speed(500)
bob.penup()
bob.goto(0,0)
bob.pendown()


bob.color("red")

for i in range (100):
	bob.forward(100)
	bob.left(170)
	bob.backward(100)
	bob.right(105)
bob.ht()
turtle.done()
