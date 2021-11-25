import turtle
import random
bob= turtle.Turtle()
bob.speed(10000)
turtle.title("TREE")

turtle.bgcolor("white")
def tree (size,level,angle,p, c,t,l):
	if level == 0 :
		bob.color(c)
		bob.begin_fill()
		bob.circle(l)
		bob.end_fill()
		bob.color(t)
		return
	bob.color(t)
	bob.pensize(p)	
	bob.forward(size)
	bob.right(angle)
	
	tree(size*0.8 ,level-1, angle, p/2,c,t,l)
	bob.left(angle*2)
	
	tree(size*0.8 ,level-1 , angle, p/2,c,t,l)
	bob.right(angle)
	bob.backward(size)
bob.penup()	
bob.goto(0,-200)
bob.forward(400)	
bob.pendown()
bob.left(90)
tree(70,7,30,15,"green", "red", 10)
def shrub():
	for i in range(20):
		bob.right(90)
		bob.forward(random.randint(40,80))
		bob.left(90)
		tree(25,4,30,7,"red", "blue", 5)
		
bob.left(90)
bob.forward(400)
bob.right(90)
tree(100,9,30,20, "pink", "black",20)
bob.left(90)
bob.forward(400)
bob.right(90)
tree(70,7,30,15, "green" ,"red",10)


bob.goto(-500,-200)	
shrub()


	
	
bob.ht()
turtle.done()
	
