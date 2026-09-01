import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("A Little Something For You")

# Setup turtle
pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.speed(2)
pen.hideturtle()

# Function to curve the top portions of the heart
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(2)

# Start drawing the heart
pen.penup()
pen.goto(0, -100) # Center the heart vertically
pen.pendown()

pen.begin_fill()
pen.left(140)
pen.forward(224)
curve()
pen.left(120)
curve()
pen.forward(224)
pen.end_fill()

# Add message
pen.penup()
pen.goto(0, -150)
pen.color("white")
# Customize the string below with her name!
pen.write("Ni hao Fine Shytt", align="center", font=("Arial", 24, "bold"))

# Keep window open
turtle.done()