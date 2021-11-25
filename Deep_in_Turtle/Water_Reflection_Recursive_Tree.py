import turtle
bob= turtle.Turtle()
bob.speed(500)
bob.getscreen().title("TREE")
bob.color("red")
turtle.bgcolor("pink")
def tree (size,level,angle,p):
	if level == 0 :
		bob.color("yellow")
		bob.begin_fill()
		bob.circle(size/2)
		bob.end_fill()
		bob.color("red")
		return
	else:
		bob.pensize(p)	
		bob.forward(size)
		bob.right(angle)
	
		tree(size*0.8 ,level-1, angle, p/2)
		bob.left(angle*2)
		
		tree(size*0.8 ,level-1 , angle, p/2)
		bob.right(angle)
		bob.backward(size)
	
	
bob.left(90)

tree(100,7,30,15)


bob.begin_fill()
bob.color("cyan")
bob.left(90)
bob.forward(360)
bob.left(90)
bob.forward(700)
bob.left(90)
bob.forward(800)
bob.left(90)
bob.forward(700)
bob.left(90)
#bob.color("cyan")
#bob.pensize(1)
bob.forward(440)

bob.end_fill()
bob.color("red")
bob.left(90)
tree(70,7,30,10)
bob.ht()
turtle.done()
	
