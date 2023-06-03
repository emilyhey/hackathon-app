from tkinter import *

def button_click():
    label.config(text="another fun fact")
    
window = st.Tk()
window.geometry("500x150")
frame = Frame(window, bd = 5)
frame.pack(side = BOTTOM, anchor = S)

leftframe = Frame(frame, bg = "black")
leftframe.pack(side=LEFT)

rightframe = Frame(frame)
rightframe.pack(side=RIGHT)

label = Label(frame, text = "fun fact", wraplength = 200)
label.pack()

button = Button(rightframe, text="click for another", command=button_click, fg="white", bg="black")
button.pack()

window.mainloop()
