import turtle
import random
bob= turtle.Turtle()
bob.speed(500)
turtle.title("TREE")
bob.color("green")
turtle.bgcolor("black")
def tree (size,level,angle,p):
	if level == 0 :
		bob.color("orange")
		bob.begin_fill()
		bob.circle(size/2)
		bob.end_fill()
		bob.color("green")
		return
	bob.pensize(p)	
	a=random.randint(20,40)
	bob.forward(size)
	
	bob.right(a)
	
	tree(size*0.8 ,level-1, a, p/2)
	bob.left(a*2)
	
	tree(size*0.8 ,level-1 , a, p/2)
	bob.right(a)
	bob.backward(size)
	
	
bob.left(90)
tree(70,7,30,15)
bob.ht()
turtle.done()
	
