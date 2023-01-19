from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f'Score:{self.current_score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def clear_score(self):
        self.clear()
