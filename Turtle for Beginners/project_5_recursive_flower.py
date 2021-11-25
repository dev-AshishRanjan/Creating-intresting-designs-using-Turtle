import turtle
bob= turtle.Turtle()
bob.speed(500)

turtle.bgcolor("cyan")
bob.color("red")

def star (s):
	if s <1:
		return 
	else:
		for i in range (5):
			
			bob.forward(10)
			bob.left(100)
			bob.forward(s)
			star(s/5)
			
				
star(200)

turtle.done()
