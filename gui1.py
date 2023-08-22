from tkinter import *

root = Tk()

root['bg'] = '#a35fc2'
root.title('Калькулятор')
root.geometry('350x500')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=350, width=500)
frame = Frame(root, bg='white')
frame.place(relx=0.15, rely= 0.15, relheight=0.7, relwidth=0.7)

title = Label(frame, text='Калькулятор', bg='grey', font=40)
title.pack()
btn1 = Button(frame, text='Button', bg='white')
btn1.pack(anchor="nw", padx=20, pady=30)

root.mainloop()