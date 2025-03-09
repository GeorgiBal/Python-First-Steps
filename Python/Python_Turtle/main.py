import turtle
hero = turtle.Turtle()
hero.speed(0)


def square(length, angle):
    for i in range(4):
        hero.forward(length)
        hero.right(angle)


for i in range(36):
    square(100, 90)
    hero.right(10)

turtle.done()
