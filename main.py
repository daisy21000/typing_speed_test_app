from tkinter import *
from typing_test import TypingTest

app = TypingTest()

window = Tk()

window.config(padx=40, pady=40)


def start_func():
    window.destroy()
    app.start_test()


title = Label(master=window, text='Typing Speed Test', font=('Ariel', 40, 'bold'))

title.pack()

start_button = Button(master=window, text='Start Typing Speed Test', command=start_func)

start_button.pack()

window.mainloop()
