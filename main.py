import turtle
from tkinter import messagebox
from turtle import Turtle,Screen
from data_analysis import states_data_analysis


#setup screen
screen = Screen() #creating screen object
screen.title("US States Game")
image = "blank_states_img.gif" #storing gif in variable
screen.addshape(image)   #it creates screen to accomodate image
turtle.shape(image)    #add image to screen

#starting count of answers
answer_count = 0
wrong_ans_count = 5

#creating data analysis object
data_analysis = states_data_analysis()


#flag for game on
game_on = True

#display at the start
messagebox.showinfo(title= "Start Game!",message =f"{wrong_ans_count} attempts remaining...")


while(game_on):

    user_input = turtle.textinput(f"{answer_count}/50 states correct" , "Enter name")

    if user_input is None:  #if user hit cancel
        break

    check_answer = data_analysis.check_state_name(user_input)
    if(check_answer):
        answer_count += 1

    elif(answer_count == 50):
        game_on = False
        data_analysis.game_over()


    else:
        wrong_ans_count -= 1
        if wrong_ans_count == 0:
            game_on = False
            data_analysis.game_over_fail()
        else:
            data_analysis.wrong_ans_warning(wrong_ans_count)






screen.exitonclick()

