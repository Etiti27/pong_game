from turtle import Turtle


# POSITION = (350, 0)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.position = position

        self.create_paddle()

    def create_paddle(self):
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.shape('square')
        self.color('white')
        self.goto(self.position)

    def move_padding_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_padding_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
