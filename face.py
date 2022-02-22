#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

from ast import Num
import turtle

# Program wide constants
WIDTH = 400
HEIGHT = 400
PEN = 1

BORDER_WIDTH = WIDTH-PEN
BORDER_HEIGHT = HEIGHT-PEN
FLOOR = BORDER_HEIGHT//6

GRASS = "#348C31"
SKY = "#add8e6"
BALL = "#ffaec8"

OBSTACLES = [
    {
        "w": 30,
        "h": 100,
        "x": 90,
        "y": FLOOR,
        "color": "#fff200"
    },
    {
        "w": 30,
        "h": 100,
        "x": 225,
        "y": FLOOR,
        "color": "#ce1927"
    },
    {
        "w": 30,
        "h": 100,
        "x": 150,
        "y": BORDER_HEIGHT - 100,
        "color": "#ce1927"
    },
    {
        "w": 30,
        "h": 100,
        "x": 300,
        "y": BORDER_HEIGHT - 100,
        "color": "#fff200"
    }
]


CLOUDS = [
    {
        "radius": 10,
        "x": 100,
        "y": 350
    },
    {
        "radius": 10,
        "x": 225,
        "y": 300
    },
    {
        "radius": 10,
        "x": 350,
        "y": 270
    },
    {
        "radius": 10,
        "x": 50,
        "y": 245
    }
]


def draw_square(t: turtle.Turtle, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.penup()


def draw_rect(t: turtle.Turtle, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.penup()


def draw_cloud(t: turtle.Turtle, radius, cloud_color="white"):
    t.color(cloud_color)

    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    t.forward(radius)
    for _ in range(4):
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.right(90)


def main():
    t = turtle.Turtle()
    s = t.getscreen()
    s.title("Game Platform")
    s.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    t.speed('fastest')

    # Draw Box around canvas
    t.pensize(PEN)
    draw_square(t, 0, 0, BORDER_WIDTH)

    # Draw platform
    t.fillcolor(GRASS)
    t.begin_fill()
    draw_rect(t, 0, 0, BORDER_WIDTH, FLOOR)
    t.end_fill()

    # Draw sky
    t.fillcolor(SKY)
    t.begin_fill()

    sky_height = BORDER_HEIGHT - (FLOOR)
    draw_rect(t, 0, FLOOR, BORDER_WIDTH, sky_height)
    t.end_fill()

    # Draw ball
    t.fillcolor(BALL)
    t.begin_fill()
    t.penup()
    t.goto(45, 150)
    t.pendown()
    t.circle(25)
    t.penup()
    t.end_fill()

    # Draw obstacles

    for obs in OBSTACLES:
        t.goto(obs["x"], obs["y"])
        t.fillcolor(obs["color"])
        t.begin_fill()
        draw_rect(t, obs["x"], obs["y"], obs["w"], obs["h"])
        t.end_fill()

    for cloud in CLOUDS:
        t.penup()
        t.goto(cloud["x"], cloud["y"])
        t.pendown()
        draw_cloud(t, cloud["radius"])

    turtle.mainloop()


main()
