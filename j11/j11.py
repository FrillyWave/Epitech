#1.1
'''
import pyjokes

print(pyjokes.get_joke('en', "chuck"))
'''
import turtle



#2.2

'''
bg = turtle.Screen()
bg.bgcolor("black")
tt = turtle.Turtle()
tt.color("red")
for i in range(4):
    tt.forward(100)
    tt.left(90)
bg.exitonclick()
'''
'''
toto = turtle . Screen () #Create a new window
toto . bgcolor ( "black" ) #Set the background color in black
titi = turtle . Turtle () #Generate a new turtle to draw
titi . color ( "red" ) #Set the drawing color in red
for i in range (3) : #3 times
    titi . right (90) #Turn right first
    titi . circle (42) #draw a circle of 42 pixels
toto . exitonclick ()   #WHen user clicks, the window shuts down
'''


def draw_polygon(sides) :
    angle = 360 / sides
    bg = turtle.Screen()
    bg.bgcolor("black")
    tt = turtle.Turtle()
    tt.color("red")
    for i in range(sides):
        tt.forward(1)
        tt.left(angle)
    bg.exitonclick()
        
#draw_polygon(1000)

#2.4
def spiral():
    bg = turtle.Screen()
    bg.bgcolor("black")
    tt = turtle.Turtle()
    tt.color("red")
    for i in range(100):
        tt.forward(1 + i)
        tt.left(15)
    bg.exitonclick()

spiral()