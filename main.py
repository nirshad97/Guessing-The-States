import turtle
import pandas
from answer_checker import Answers

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
states = pandas.read_csv("50_states.csv")

states_list = states['state'].tolist()


game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title=f"{50 - len(states_list)} out of 50, guessed", prompt="What's another state?")

    # After the input the below condition checks for the membership
    if answer_state.title() in states_list:
        x_cor = states[states['state'] == answer_state.title()]['x']  # This grabs the x coordinate from the dataframe
        y_cor = states[states['state'] == answer_state.title()]['y']  # This grabs the y coordinate from the dataframe
        ans = Answers(x_cor,y_cor, answer_state)
        states_list.remove(answer_state.title()) # This removes input state from the list
        # We can keep record of the states and it's count. One the length reaches zero, while loop will break
        if len(states_list) == 0:
            game_is_on = False
    else:
        pass

screen.exitonclick()



