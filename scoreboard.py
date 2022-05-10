from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
GAME_OVER_FONT = ('Arial', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color('white')
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=GAME_OVER_FONT)

    def update_scoreboard(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()






