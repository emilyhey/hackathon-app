import streamlit as st
from tkinter import *

window = Tk()
window.geometry("500x150")
frame = frame(window, anchor = S)
frame.pack()

leftframe = Frame(window, bg = "black", bd = "5")
leftframe.pack(side=LEFT)
 
rightframe = Frame(window)
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "fun fact", wraplength = 1)
label.pack()

button = Button(rightframe, text="click for another", command=button_click, font="white")
button.pack()

window.mainloop()
