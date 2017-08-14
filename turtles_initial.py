import turtle

window = turtle.Screen()
window.bgcolor("green")
brad = turtle.Turtle()
brad.shape("circle")
brad.color("yellow")
brad.speed(0)

def draw_K() :
    brad.left(90)
    brad.forward(150)
    brad.penup()
    coords = brad.position()
    brad.goto(coords[0] + 70, coords[1])
    brad.pendown()
    brad.left(135)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    

def draw_M() :
    brad.left(90)
    brad.forward(150)
    brad.right(135)
    brad.forward(70)
    brad.left(90)
    brad.forward(70)
    brad.right(135)
    brad.forward(150)

def draw_C() :
    coords = brad.position()
    brad.penup()
    brad.goto(coords[0] + 50, coords[1])
    brad.pendown()
    brad.left(180)
    brad.forward(50)
    brad.right(90)
    brad.forward(150)
    brad.right(90)
    brad.forward(50)
    
def give_space() :
    brad.penup()
    space_coords = brad.position()
    brad.goto(space_coords[0] + 50, 0)
    brad.setheading(0)
    brad.pendown()

draw_K()
give_space()
draw_M()
give_space()
draw_C()
