from tkinter import *
from tkinter.ttk import Button

def window2(root):
    def window1():
        print("hi")
        root.destroy()
    root.destroy()
    root = Tk()
    root.geometry("200x200+100+100")
    Label(root, text="second screen").pack()
    a = Button(text="Click This", command = window1)
    a.bind
    a.pack()
    root.mainloop()
    return 3
