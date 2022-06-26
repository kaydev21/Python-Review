# SquareSpiral4.py
import turtle
t = turtle.Pen()
turtle.bgcolor("light blue")
t.speed(0)
sides = 6
colors = ["red", "yellow", "green", "blue", "magenta","cyan"]
for x in range(360):
    t.pencolor( colors[x%sides])
    t.forward(x * 3 / sides + 1)
    t.left(360/sides + 1)
    t.width(x*sides/100)