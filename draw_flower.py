import turtle

def draw_flower(ink):
    ink.up()
    ink.home()
    for degrees in range(10, 370, 10):
        ink.down()
        ink.forward(200)
        ink.up()
        ink.home()  # resets angle to 0 degrees
        ink.left(degrees)


def draw_stem(stem):

    stem.goto(1, -400)
    stem.home()
    stem.goto(5, -400)
    stem.home()
    stem.goto(3, -400)


def flower():


    window = turtle.Screen()
    window.bgcolor('green')

    stem = turtle.Turtle()
    stem.color('yellow')
    stem.speed('fast')

    draw_stem(stem)

    flo = turtle.Turtle()
    flo.color('white')
    flo.speed('fastest')

    draw_flower(flo)

    window.exitonclick()


flower()
