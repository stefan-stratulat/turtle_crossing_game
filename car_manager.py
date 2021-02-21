from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.cars = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.setheading(180)
        new_car.hideturtle()
        new_car.x_cor = 280
        new_car.y_cor = random.randint(-240,280)
        new_car.goto(new_car.x_cor,new_car.y_cor)
        self.cars.append(new_car)

    def increase_car_speed(self):
        self.moving_distance += MOVE_INCREMENT

    def move_car(self):
        for car in self.cars[::3]:
            car.showturtle()
            car.forward(self.moving_distance)
