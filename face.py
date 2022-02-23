#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

from time import sleep
from tkinter import PhotoImage
import turtle
import math

# Program wide constants
WIDTH = 400
HEIGHT = 400
PEN = 1

BORDER_WIDTH = WIDTH-PEN
BORDER_HEIGHT = HEIGHT-PEN
FLOOR = BORDER_HEIGHT//6

GRASS = "#77DD77"
SKY = "#add8e6"

BIRD = "bird.gif"

OBSTACLES = [
    {
        "w": 30,
        "h": 100,
        "x": 87,
        "y": FLOOR,
        "color": "orange"
    },
    {
        "w": 35,
        "h": 25,
        "x": 200,
        "y": FLOOR,
        "color": "#ce1927"
    },
    {
        "w": 70,
        "h": 16,
        "x": 310,
        "y": FLOOR,
        "color": "orange"
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
        "color": "orange"
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
    '''
        Draws a square of the provided size starting at the given (x,y) coordinates on the lower left
    '''
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.penup()


def draw_rect(t: turtle.Turtle, x, y, width, height):
    '''
        Draws a rectangle of the provided size starting at the given (x,y) coordinates on the lower left
    '''
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.penup()


def draw_cloud(t: turtle.Turtle, radius, x, y, cloud_color="white"):
    '''
        Draws a cloud of the provided radius at the (x,y) coordinates
    '''
    t.penup()
    t.goto(x, y)
    t.pendown()

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


def draw_bird(bird: turtle.Turtle, bird_x, bird_y):
    '''
        Draws a bird to the screen
    '''
    bird.penup()
    bird.goto(bird_x, bird_y)


def draw_arc(t, x, y, r, pensize, color):
    '''
        Draw a colored arc
    '''
    t.up()
    t.goto(x+r, y)
    t.down()
    t.seth(90)
    t.pensize(pensize)
    t.pencolor(color)
    t.circle(r, 180)


def draw_rainbow(t):
    '''
        Draw a 7 color rainbow
    '''
    radius = (BORDER_WIDTH//2)-3
    penwidth = 7
    for col in ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']:
        draw_arc(t, 200, FLOOR+PEN, radius, penwidth, col)
        radius -= (penwidth-1)


def setup(t: turtle.Turtle):
    '''
        Draws all the non moving objects to the screen
    '''
    # Draw Border of canvas
    t.pensize(PEN)
    draw_square(t, 0, 0, BORDER_WIDTH)

    # Draw sky
    t.fillcolor(SKY)
    t.begin_fill()
    sky_height = BORDER_HEIGHT - (FLOOR)
    draw_rect(t, 0, FLOOR, BORDER_WIDTH, sky_height)
    t.end_fill()

    # Draw rainbow
    r = turtle.Turtle()
    draw_rainbow(r)

    # Draw floor
    t.fillcolor(GRASS)
    t.begin_fill()
    t.pencolor("green")
    draw_rect(t, 0, 0, BORDER_WIDTH, FLOOR)
    t.end_fill()
    t.pencolor("black")

    # Draw Obstacles
    for obs in OBSTACLES:
        t.goto(obs["x"], obs["y"])
        t.fillcolor(obs["color"])
        t.begin_fill()
        draw_rect(t, obs["x"], obs["y"], obs["w"], obs["h"])
        t.end_fill()

    # Draw Clouds
    for cloud in CLOUDS:
        draw_cloud(t, cloud["radius"], cloud["x"], cloud["y"])


def animate(t: turtle.Turtle, s: turtle.Screen, FPS):
    '''
        Draws all the moving objects to the screen
    '''
    for i in range(12):
        t.clear()
        amp = 8
        x = 45 + (i*30)
        y = 150 + (math.sin(i)) * (2*math.pi*amp)
        draw_bird(t,  x,  y)
        s.update()
        sleep(1/FPS)
    t.reset()


def main():
    # Initalize window
    s = turtle.Screen()
    s.tracer(0)
    s.title("Flappity Bird")
    s.setworldcoordinates(0, 0, WIDTH, HEIGHT)

    # Turtle for drawing background
    bg = turtle.Turtle()
    bg.speed('fastest')
    setup(bg)

    # Moving bird turtle
    smaller = PhotoImage(file=BIRD).subsample(12, 12)
    s.addshape(smaller, turtle.Shape("image", smaller))
    bird = turtle.Turtle(smaller)

    while True:
        animate(bird, s, 10)


main()
