import streamlit as st
import Tkinter as tk


def button_click():
    label.config(text="another fun fact")

window = st.tk.Tk()
window.geometry("500x150")
frame = tk.Frame(window, bd = 5)
frame.pack(anchor = tk.S)

leftframe = tk.Frame(frame, bg = "black")
leftframe.pack(side=tk.LEFT)

rightframe = tk.Frame(frame)
rightframe.pack(side=tk.RIGHT)

label = tk.Label(frame, text = "fun fact", wraplength = 200)
label.pack()

button = tk.Button(rightframe, text="click for another", command=button_click, fg="white", bg="black")
button.pack()

window.mainloop()
