from turtle import  Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.left_score}", align="center", font=("Courier", 18, "normal"))
        self.goto(100, 250)
        self.write(f"{self.right_score}", align="center", font=("Courier", 18, "normal"))


