import turtle
import cmasher as cm
import matplotlib
import colorsys


bob = turtle.Turtle()
bob.speed("fastest")
turtle.bgcolor("black")

def circles(size):
	for i in range (10):
		bob.circle(size)
		size -=4
		
def design( size, repeat):
	for i in range (repeat):
		circles(size)
		bob.right(360/repeat)
	
		
		
#colors = ["white", "yellow", "blue", "red", "pink"]
colors= cm.take_cmap_colors('viridis', 300 , return_fmt = 'hex')

def final (size,repeat):
	for i in colors :
		bob.color(i)
		design (size, repeat)
		size /=1.3
final(150,10)
	

turtle.done()
