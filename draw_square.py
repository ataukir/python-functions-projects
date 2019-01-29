import turtle


def draw_square(brad):
    for i in range(1, 90):
        for i in range(1, 5):
            brad.forward(100)
            brad.right(90)
        brad.right(5)


def draw_circle(angie):
    angie.circle(100)


def draw_tri(tri):
    for i in range(3):
        tri.forward(90)
    tri.left(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('green')
    # creating the turtle brad - draw square
    brad = turtle.Turtle()


    brad.shape('turtle')
    brad.color('yellow')
    brad.speed('fastest')
    draw_square(brad)

    # creating the angie - draw circle
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.speed('fast')
    angie.color('yellow')
    draw_circle(angie)
    #
    # # creating the turtle tri - draw triangle
    tri = turtle.Turtle()
    tri.color('yellow')
    tri.speed('fast')
    draw_tri(tri)

# exit window on clickk
    window.exitonclick()

draw_art()
