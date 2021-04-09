import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:

            if state in guess_state:
                pass
            else:
                missing_state.append(state)

        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("missing_guess_state")
        break

    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data.state.item())
