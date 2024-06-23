#Calculator app using Tkinter library
from tkinter import * #import tkinter library
import ast
root = Tk() #creating the window using tk() class inside tkinter library

#creating a function when button clicked and it should type in the ENTRY WIDGET
index = 0
def get_number(num):
    global index
    user_entry.insert(index, num)
    index = index+1

def get_operator(op):
    global index
    length = len(op)
    user_entry.insert(index, op)
    index = index+length

def calculate(num, op):
    global index
    sum = num+op
    user_entry.insert(index, sum)

def clear_all():
    user_entry.delete(0, END)

def calculate():
    try:
        entire_value = user_entry.get()
        parsed_entire_value = ast.parse(entire_value, mode='eval')
        result = eval(compile(parsed_entire_value, '<string>', 'eval'))
        clear_all()
        user_entry.insert(0, result)
    except Exception:
        clear_all()
        user_entry.insert(0, "Error!")



def backspace():
    entire_string = user_entry.get()
    if len(entire_string): #So,in python, if len(entire_string): is equivalent to if len(entire_string) > 0:. Both will evaluate to True if the string length is greater than zero and False if the string is empty.
        new_string = entire_string[:-1]
        clear_all()
        user_entry.insert(0, new_string)
    else:
        user_entry.insert(0, "")


user_entry = Entry(root) # creating an ENTRY used for user input widget
user_entry.grid(row=1,columnspan=6) # column_span is used to stretch the ENTRY widget until 6 column, It will occupy the entire second row, stretching from the first column to the sixth column.


#creating a 3 by 3 grid placing button inside them
#numbers = [1,2,3,4,5,6,7,8,9]
counter = 1
for x in range(3):
    for y in range(3):
        #button_text = numbers[counter]
        create_button = Button(root, text=counter, width=3, height=3, background="grey", foreground="white", command= lambda text=counter : get_number(text))
        create_button.grid(row=x+2, column=y)
        counter = counter+1

create_zero_button = Button(root, text="0", width=3, height=3, background="grey", foreground="white", command= lambda text = "0" :get_number(text))
create_button_for_plus = Button(root, text="+/-", width=3, height=3, background="grey", foreground="white", command= lambda text = "+/-" :get_number(text))
create_button_for_dot = Button(root, text=".", width=3, height=3, background="grey", foreground="white", command= lambda text = "." :get_number(text))
create_zero_button.grid(row=5, column=1)
create_button_for_plus.grid(row=5, column=0)
create_button_for_dot.grid(row=5, column=2)

#creating other button/operator button
count =0
operations = ["+", "-", "*", "/", "(", ")", "**", "**2"]
for x in range(4):
    for y in range(3):
        if count<len(operations):
            create_operator_button = Button(root, text=operations[count], width=3, height=3, background="dark grey", foreground="white", command=lambda text=operations[count] : get_operator(text))
            count = count+1
            create_operator_button.grid(row=x+2, column=y+3)

create_CE_button = Button(root, text="CE", width=3, height=3, background="blue", foreground="white", command=clear_all)
create_EQUAL_button = Button(root, text="=", width=3, height=3, background="green", foreground="white",command=calculate)
create_backspace_button = Button(root, text="<=", width=3, height=3, background="red", foreground="white",command=backspace)
create_CE_button.grid(row=5, column=4)
create_EQUAL_button.grid(row=5, column=5)
create_backspace_button.grid(row=5, column=3)




