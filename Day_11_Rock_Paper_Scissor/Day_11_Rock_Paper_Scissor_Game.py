#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import random 
import tkinter  

#Create Object for the UI
root = tkinter.Tk() 
 
#Set geometry of the frame
root.geometry("500x350") 
 
#Set title of the frame 
root.title("Rock-Paper-Scissors Game") 

#Computer Value 
computer_dict = { 
"0":"Rock", 
"1":"Paper", 
"2":"Scissors" 
} 


#Reset the game 
def reset_game(): 
    b1["state"] = "active" 
    b2["state"] = "active" 
    b3["state"] = "active" 
    l1.config(text = "Player			 ") 
    l3.config(text = "Computer") 
    l4.config(text = "") 


#Disable the button 
def button_disable():
    b1["state"] = "disable" 
    b2["state"] = "disable" 
    b3["state"] = "disable" 



#If player selects rock 
def player_rock(): 
    c_v = computer_dict[str(random.randint(0,2))] 
    if c_v == "Rock": 
        match_result = "Tie!" 
    elif c_v=="Scissors": 
        match_result = "Player Wins" 
    else: 
        match_result = "Computer Wins" 
    l4.config(text = match_result) 
    l1.config(text = "Rock		 ") 
    l3.config(text = c_v) 
    button_disable() 

#If player selects paper 
def player_paper(): 
    c_v = computer_dict[str(random.randint(0, 2))] 
    if c_v == "Paper": 
        match_result = "Tie!" 
    elif c_v=="Scissors": 
        match_result = "Computer Wins" 
    else: 
        match_result = "Player Wins" 
    l4.config(text = match_result) 
    l1.config(text = "Paper		") 
    l3.config(text = c_v) 
    button_disable() 

#If player selects scissors 
def player_scissors(): 
    c_v = computer_dict[str(random.randint(0,2))] 
    if c_v == "Rock": 
        match_result = "Computer Wins" 
    elif c_v == "Scissors": 
        match_result = "Tie!" 
    else: 
        match_result = "Player Wins" 
    l4.config(text = match_result) 
    l1.config(text = "Scissors		 ") 
    l3.config(text = c_v) 
    button_disable() 

    
#Adding Labels, Frames and Button 
tkinter.Label(root,           
    text =("------ Choose any one : Rock / Paper / Scissors ----- \n"), 
    font = "Jost", 
    fg = "#000000").pack(pady = 15)  


frame = tkinter.Frame(root) 
frame.pack() 

l1 = tkinter.Label(frame, 
    text = "Player ", 
    font = 10,
    fg = "#150050") 

l2 = tkinter.Label(frame, 
    text = "   VS   ", 
    font = "Lobster",               
    fg = "#1A132F") 

l3 = tkinter.Label(frame, 
    text = "Computer", 
    font = 10,
    fg = "#150050") 

l1.pack(side = 'left') 
l2.pack(side = 'left') 
l3.pack(side = 'right') 

l4 = tkinter.Label(root, 
        text = "", 
        font = "Lobster", 
        bg = "#FEFBF3", 
        width = 15 , 
        borderwidth = 2, 
        relief = "solid") 
l4.pack(pady = 20) 

frame1 = tkinter.Frame(root) 
frame1.pack() 
b1 = tkinter.Button(frame1, text = "Rock", 
            font = 8, width = 7, fg = "#3F0071", bg = "white",
            command = player_rock) 

b2 = tkinter.Button(frame1, text = "Paper ", 
            font = 8, width = 7, fg = "#3F0071", bg = "white",
            command = player_paper) 

b3 = tkinter.Button(frame1, text = "Scissors", 
            font = 8, width = 7, fg = "#3F0071", bg = "white",
            command = player_scissors) 

b1.pack(side = 'left', padx = 10) 
b2.pack(side = 'left', padx = 10) 
b3.pack(padx = 10) 

tkinter.Button(root, text = "Reset Game", 
        font = 10, fg = "#610094", 
        bg = "white", command = reset_game).pack(pady = 20) 

#Execute Tkinter 
root.mainloop() 


# In[ ]:




