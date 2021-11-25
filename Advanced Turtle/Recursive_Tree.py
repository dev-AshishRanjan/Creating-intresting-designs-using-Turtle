import turtle
bob= turtle.Turtle()
bob.speed(500)
turtle.title("TREE")
bob.color("blue")
turtle.bgcolor("red")
def tree (size,level,angle,p):
	if level == 0 :
		bob.color("yellow")
		bob.begin_fill()
		bob.circle(size/2)
		bob.end_fill()
		bob.color("blue")
		return
	bob.pensize(p)	
	bob.forward(size)
	bob.right(angle)
	
	tree(size*0.8 ,level-1, angle, p/2)
	bob.left(angle*2)
	
	tree(size*0.8 ,level-1 , angle, p/2)
	bob.right(angle)
	bob.backward(size)
	
	
bob.left(90)
tree(70,7,30,15)
bob.ht()
turtle.done()
	
