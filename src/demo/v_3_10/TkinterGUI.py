import tkinter as tk
from tkinter import IntVar, Checkbutton, Label, Entry, LEFT, RIGHT
from tkinter import messagebox

top = tk.Tk()


# Code to add widgets will go here...
def hello_call_back():
    messagebox.showinfo("Hello Python", "Hello World")


B = tk.Button(top, text="Hello", fg="blue", command=hello_call_back)
B.pack()

C = tk.Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(
    top, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20
)
C2 = Checkbutton(
    top, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20
)
C1.pack()
C2.pack()

L1 = Label(top, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)

top.mainloop()
