import turtle
import math

def draw_branch(t, length, angle, level):
    if level == 0:
        return
    t.forward(length)
    t.left(angle)
    draw_branch(t, length * 0.7, angle, level - 1)
    t.right(2 * angle)
    draw_branch(t, length * 0.7, angle, level - 1)
    t.left(angle)
    t.backward(length)

def draw_pythagoras_tree(level):
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_branch(t, 100, 30, level)
    screen.mainloop()

# Задайте рівень рекурсії тут
recursion_level = 6
draw_pythagoras_tree(recursion_level)