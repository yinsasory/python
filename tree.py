import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)
        t.left(40)
        draw_branch(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def draw_tree():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(2)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    draw_branch(75, t)
    screen.exitonclick()

draw_tree()
