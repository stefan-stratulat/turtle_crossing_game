from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.level = 1
        self.write(f"Level: {self.level} ",font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level} ",font=FONT)

    def game_over(self):
        self.color('black')
        self.hideturtle()
        self.penup()
        self.write('GAME OVER.', font=FONT)
        self.goto(0,0)



