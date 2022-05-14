from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
GAME_OVER_FONT = ('Arial', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color('white')
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=GAME_OVER_FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open('high_score.txt', mode='w') as data:
            data.write(f'{self.high_score}')






