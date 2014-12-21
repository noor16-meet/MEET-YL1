import turtle
input("Let's Draw!")
input("Instructions: button left = color blue button down = yellow button up = green , to draw triangle= press on right click, to draw square= press on left click, and whenever you want to start over press c now press c to start drawing")
def erase():
	turtle.clear()
turtle.getscreen().onkeypress(erase,"c")
turtle.getscreen().listen()

turtle.pd()
x,y=turtle.position()

	
def draw_square(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pd()
	turtle.goto(x+20,y)
	turtle.goto(x+20,y+20)
	turtle.goto(x,y+20)
	turtle.goto(x,y)
draw_square(x,y)

def draw_triangle(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pd()
	turtle.goto(x+25,y+50)
	turtle.goto(x+50,y)
	turtle.goto(x,y)
draw_triangle(20,20)



turtle.onscreenclick(draw_square, btn=1, add=True)
turtle.onscreenclick(draw_triangle, btn=3, add=True)

turtle.color("red")	
turtle.onscreenclick(turtle.goto, btn=1, add=True)
turtle.shape("turtle")
def green():turtle.color("green")
turtle.getscreen().onkeypress(green,"Up")
turtle.getscreen().listen()

def yellow():turtle.color("yellow")
turtle.getscreen().onkeypress(yellow,"Down")
turtle.getscreen().listen()

def blue():turtle.color("blue")
turtle.getscreen().onkeypress(blue,"Left")
turtle.getscreen().listen()

def triangle():turtle.shape("square")
turtle.getscreen().onkeypress(triangle,"space")
turtle.getscreen().listen()





	
turtle.mainloop()


