import turtle
import pandas
screen=turtle.Screen()
screen.title(f"U.S States Game")
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
is_true=False
dict_data=pandas.read_csv('./50_states.csv')
all_states=dict_data['state'].to_list()

guess=[]
while len(guess)<50:
    answer = screen.textinput(title=f"{len(guess)}/50 States correct", prompt="what's another state's name?").title()
    if answer in all_states:
        guess.append(answer)
        new=turtle.Turtle()
        new.penup()
        new.hideturtle()
        state_data=dict_data[dict_data.state == answer]
        new.goto(int(state_data['x']),int(state_data['y']))
        new.write(f"{answer}")
    if answer == 'Exit':

        #using list comprehension:

        guess_not=[state for state in all_states if state not in guess]
        new_data=pandas.DataFrame(guess_not)
        new_data.to_csv("states_to_learn.csv")
        break
screen.exitonclick()