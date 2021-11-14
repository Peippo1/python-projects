from turtle import Turtle, Screen

# Basic etch-a-sketch game made for learning oop with python using Turtle

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.backward(10)


def turn_left():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)


def turn_right():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
# note that we dont calll the parameters of the move_forwards function as we are waiting to initiate the function not calling it directly.
screen.exitonclick()
