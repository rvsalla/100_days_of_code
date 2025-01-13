import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r".\Day_25\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

lable = turtle.Turtle()
lable.hideturtle()
lable.penup()

#get coordnates on screen
#def get_mouse_cord(x,y):
#    print(x, y)
#turtle.onscreenclick(get_mouse_cord)
#turtle.mainloop()

states_data = pd.read_csv(r'.\Day_25\50_states.csv')
correct_ansewer = []
missing_states = []

while len(correct_ansewer) < len(states_data):
    ansewer_state = screen.textinput(title=f'{len(correct_ansewer)}/{len(states_data)} States Correct', prompt= "What's another state name?").title()

    if ansewer_state =='Exit':
        break

    for index, row in states_data.iterrows():
        if ansewer_state == row["state"]:
            correct_ansewer.append(row["state"])
            lable.goto(row["x"], row["y"])
            lable.write(row["state"], font=('courrier', 8))

#for index, row in states_data.iterrows():
#    if row["state"] not in correct_ansewer:
#        missing_states.append(row["state"])

missing_states = [row["state"] for index, row in states_data.iterrows() if row["state"] not in correct_ansewer]


states_to_learn_df = pd.DataFrame(missing_states, columns=["states_to_learn"])
states_to_learn_df.to_csv(".\Day_25\states_to_learn.csv", index=False)



