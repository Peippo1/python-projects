# simple Pong game in Python 3 for beginners 
# little OOP 
# code originally from @TokyoEdTech and from FreeCodeCamp


import turtle
import os

wn = turtle.Screen() #screen def wn
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set to maximum speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # prevents line tracing
paddle_a.goto(-350, 0) #beginning location from paddle_a


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set to maximum speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # prevents line tracing
paddle_b.goto(+350, 0) #beginning location from paddle_b

# Ball
ball = turtle.Turtle()
ball.speed(0) # set to maximum speed
ball.shape("square")
ball.color("white")
ball.penup() # prevents line tracing (drawing a line when the object moves)
ball.goto(0, 0) #beginning location from paddle_a
# ball speed move by 2px on axis
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))





# Functions for game play
# paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Functions for game play
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Functions for game play
# paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Functions for game play
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# Main game loop
while True:
    wn.update() # everytime that the program runs it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking - setting a frame for the ball to 'bounce' off
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # this will reverse the direction of the ball
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # this will reverse the direction of the ball
        os.system("afplay bounce.wav&")


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        # this is how we are updating the score ^ 

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        # this is how we are updating the score ^ 
        


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
