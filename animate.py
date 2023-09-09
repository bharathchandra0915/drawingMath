import turtle
import time

def go_to_left(starting_point):
    t.penup()
    x,y = starting_point
    t.goto(x-screen.window_width() / 2  , -(y- screen.window_height() / 2 )) 
    t.pendown()

def go_to_right(starting_point, a):
    t.penup()
    x,y = starting_point
    t.goto(x-screen.window_width() / 2 +a  , -(y- screen.window_height() / 2 )) 
    t.pendown()


def draw_sides(length, angle, direction = "right"):
    t.color("red")
    print("drawing sides")
    t.setheading(0)
    t.penup()
    if direction == "right":
        
        t.setheading(180)
        t.right(angle)
    elif direction == "left":
        t.left(angle)
    t.pendown()
    t.forward(length)
    

def draw_arc(radius, direction = "right"):
    t.setheading(0)  ## sets the cursor directoin to right
    t.left(90)
    t.penup()
    t.forward(radius)
    t.pendown()
    if direction == "right":
        t.left(90)
        t.circle(radius, 90)
    elif direction == "left":
        t.right(90)
        t.circle(-radius, 90)

def draw_base(start_point, a):
    t.penup()  
    go_to_left(starting_point=start_point)
    t.setheading(0)

    t.pendown()  
    t.forward(a)

def draw_on_canvas(start_point, a, b, c, angles):
    draw_base(start_point, a)

    draw_arc(b, direction = "right")
    go_to_left(starting_point=start_point)    
    draw_arc(c, direction ="left")

    go_to_right(start_point, a)
    draw_sides(b, angles[2], "right")
    go_to_left(start_point)
    draw_sides(c, angles[1], "left")




screen = turtle.Screen()
screen.setup(width=640, height=480)
screen.bgcolor('black')
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.color('white')
