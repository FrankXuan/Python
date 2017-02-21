import turtle


def draw_square(some_turtle):
    for s in range(1,40):
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)
        some_turtle.right(10)
        s += 1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    # create the turtle brad - and draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(20)
    draw_square(brad)

    # create the turtle brad - and draw a circle
    # frank = turtle.Turtle()
    # frank.shape("arrow")
    # frank.color("blue")
    # frank.speed(100)
    # frank.circle(100, 360)

    window.exitonclick()


draw_art()
