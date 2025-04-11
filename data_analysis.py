#check if single guess is state
from tkinter import messagebox

import pandas
from turtle import Turtle


data = pandas.read_csv("50_states.csv") #reading data from csv
state_list = data.state.to_list()  #fetching states as a list

class states_data_analysis(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

#checking name of state whether it is correct or not
    def check_state_name(self,input):

        input = input.lower()

        for state in state_list:
            if state.lower() == input:
                state_data = data[data.state.str.lower() == input] #fetching matched state row
                #print(state_data) #for debugging(state_name , x-co , y-co)
                self.goto(state_data.x.item() , state_data.y.item()) #goto x-co and y-co
                self.write(state) #write state name on x-co and y-co
                state_list.remove(state) #removing state from list for eliminating double count
                return True


#warning player about wrong answer
    def wrong_ans_warning(self,count):
        messagebox.showinfo(title= "Wrong Answer!!!",message =f"{count} attempts remaining...")


#game over Function after giving all the answers correctly
    def game_over(self):
        self.goto(0,0)
        self.write("You completed the game!", False , "center" ,("Arial" , 20 , "bold"))

#ending game bcoz of excessive incorrect answers(5)
    def game_over_fail(self):
        self.goto(0,0)
        self.write("You failed to complete the game!", False , "center" ,("Arial" , 20 , "bold"))