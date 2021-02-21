from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car()

    def car(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.setheading(180)