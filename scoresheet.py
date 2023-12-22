from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(100, 200)
        self.write(f'{self.l_score}', align='center', font=('Arial', 50, 'normal'))
        self.goto(-100, 200)
        self.write(f'{self.r_score}', align='center', font=('Arial', 50, 'normal'))

    def scoreline_left(self):
        self.l_score += 1
        self.update_score()

    def scoreline_right(self):
        self.r_score += 1
        self.update_score()
