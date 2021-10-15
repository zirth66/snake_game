from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 30, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font = FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font = FONT, align=ALIGNMENT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        