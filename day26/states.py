import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US states game")
image = "day25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []
answer = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
data = pd.read_csv("day25/50_states.csv")
states = data.state.to_list()
game_is_on = True
while game_is_on:
    if answer == 'Exit':
        states_to_learn = [x for x in states if x not in guessed_states]

        df = pd.DataFrame(states_to_learn)
        df.to_csv("day25/states_to_learn.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        states.remove(answer)
    if len(guessed_states) == 50:
        game_is_on = False
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()



df = pd.DataFrame(states_to_learn)

turtle.mainloop()