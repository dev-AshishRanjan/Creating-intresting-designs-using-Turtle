import turtle
bob= turtle.Turtle()
bob.speed(500)
turtle.title("TREE")
bob.color("black")
turtle.bgcolor("white")
def tree (size,level,angle,p):
	if level == 0 :
		bob.color("pink")
		bob.begin_fill()
		bob.circle(size/3)
		bob.end_fill()
		bob.color("black")
		return
	bob.pensize(p)	
	bob.forward(size)
	bob.right(angle)
	
	tree(size*0.8 ,level-1, angle, p/2)
	bob.left(angle)
	
	tree(size,level-1 , angle, p/2)
	bob.left(angle)
	tree(size*0.8, level-1, angle, p/2)
	bob.right(angle)
	
	bob.backward(size)
	
	
bob.left(90)
tree(70,5,30,15)
bob.ht()
turtle.done()
