from words import test_words
from tkinter import *
import random


class TypingTest:
    def __init__(self):
        self.words = test_words
        self.window = None
        self.canvas = None
        self.index = 0
        self.time_display = None
        self.word_label = None
        self.word_input = None
        self.restart_button = None
        self.seconds = 60
        self.valid_chars = 0
        self.valid_words = 0
        self.timer = None

    def start_test(self):
        if self.window:
            self.window.destroy()
        self.window = Tk()
        self.generate_words()
        self.canvas = Canvas(width=600, height=300)
        self.time_display = self.canvas.create_text(590, 280, text=0)
        self.word_label = self.canvas.create_text(300, 150, text='Word', font=('Ariel', 30, 'bold'))
        self.word_input = Entry(width=40)
        self.word_input.bind('<space>', self.check_word_is_valid)
        self.show_new_word()
        self.canvas.pack()
        self.word_input.pack()
        self.countdown(60)
        if self.seconds == 0:
            self.window.mainloop()

    def generate_words(self):
        random.shuffle(self.words)

    def show_new_word(self):
        try:
            word = self.words[self.index]
        except IndexError:
            self.index = 0
            word = self.words[self.index]
        self.canvas.itemconfig(self.word_label, text=word)
        self.word_input.delete(0, END)

    def check_word_is_valid(self, key):
        word_input = self.word_input.get().strip().lower()
        word = self.words[self.index].lower()
        self.index += 1
        self.show_new_word()
        if word == word_input:
            self.valid_words += 1
            self.valid_chars += len(word)
        if self.seconds == 0:
            self.canvas.itemconfig(self.word_label, text=f'Words Per Minute: {self.valid_words}\nCharacters Per Minute: {self.valid_chars}')
            self.word_input.pack_forget()
            self.restart_button = Button(text='Restart Test', command=self.start_test)
            self.restart_button.pack()

    def countdown(self, count):
        self.seconds = count
        if self.seconds > 0:
            self.timer = self.window.after(1000, self.countdown, count - 1)
        else:
            self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.time_display, text=self.seconds)
