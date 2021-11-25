#Courtesy: Keith
import turtle
bob= turtle.Turtle()
bob.speed(50)

turtle.bgcolor("cyan")
bob.color("red")

def star (size):
	if size <10:
		return
	else:
		for i in range (5):
			
			bob.forward(size)
			star(size/3)
			bob.left(216)
				
star(200)

turtle.done()
