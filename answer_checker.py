from turtle import Turtle
# This class creates objects of letters corresponding to the states


class Answers(Turtle):

    def __init__(self, x_cor, y_cor, name_of_state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(int(x_cor), int(y_cor))
        self.write(f"{name_of_state.title()}")




