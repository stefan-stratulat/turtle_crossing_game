from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []

    def generate_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.setheading(180)
        new_car.hideturtle()
        new_car.x_cor = 280
        new_car.y_cor = random.randint(-260,280)
        new_car.goto(new_car.x_cor,new_car.y_cor)
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars[::3]:
            car.showturtle()
            car.forward(MOVE_INCREMENT)