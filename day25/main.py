import turtle

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer = screen.textinput(title="Guess the state", prompt="What's another state's name?")

turtle.mainloop()