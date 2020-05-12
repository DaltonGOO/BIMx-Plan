
import pandas as pd
import tkinter as tk
from flask import Flask 
import flask_sqlalchemy
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

# tkinter GUI
root= tk.Tk()
button = tk.Button(root, text = 'Click Me')

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# Username label and input box
label1 = tk.Label(root, text='Username ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 100, window=entry1)


# Project_Number label and input box
label2 = tk.Label(root, text='Project number ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)




def values(): 
    global Username #our 1st input variable
    Username = str(entry1.get()) 
    
    global Project_Number #our 2nd input variable
    Project_Number = str(entry2.get()) 
    
    return[Username, Project_Number]




def BIMdata():
    data = [values()]
    df = pd.DataFrame(data, columns = ['Username', 'Project Number']) 
    df.to_csv('myprojectinfo.csv', mode='a', header=False)



button1 = tk.Button (root, text='Finished',command= BIMdata, bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)





button.pack()
root.mainloop()

















