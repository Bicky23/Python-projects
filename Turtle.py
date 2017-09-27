import turtle

def draw_square(animal):
    for i in range(1,5):
        animal.forward(100)
        animal.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('blue')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_shapes()
