from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score+1}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)

    def keep_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

