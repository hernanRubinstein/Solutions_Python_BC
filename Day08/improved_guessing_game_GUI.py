import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

        self.number = random.randrange(1, 21)
        self.counter = 0

        self.label = tk.Label(root, text="Rules of game:\nIn each moment you can exit the game press: 'x'\nTo restart press: 'n'\nTo get the current answer (Cheating) press: 's'")
        self.label.pack()

        self.guess_label = tk.Label(root, text="Please write your guess:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()
        self.guess_entry.bind("<Return>", self.process_guess)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.process_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack()

        self.exit_button = tk.Button(root, text="Exit Game", command=root.quit)
        self.exit_button.pack()

    def process_guess(self, event=None):
        user_input = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)
        
        if self.special_key(user_input) == "Continue":
            self.counter += 1
            try:
                result = self.evaluate_input(user_input)
                self.result_label.config(text=result)
                if result == "Restarting" or result == "Exiting Game":
                    self.end_game(result)
            except ValueError:
                self.result_label.config(text="Please enter a valid input")
        else:
            self.end_game(self.special_key(user_input))

    def special_key(self, user_input):
        if user_input.lower() == 'x':
            return "Exiting Game"
        elif user_input.lower() == 'n':
            if messagebox.askyesno("New Game", "New game? [yes/no]"):
                return "Restarting"
            else:
                return "Exiting Game"
        elif user_input.lower() == 's':
            self.result_label.config(text=f"The answer is: {self.number} You cheater")
            return "Guess again"
        else:
            return "Continue"

    def evaluate_input(self, user_input):
        if int(user_input) == self.number:
            result = f"GREATTT!\nGuesses #: {self.counter}"
            if messagebox.askyesno("New Game", "New game? [yes/no]"):
                return "Restarting"
            else:
                return "Exiting Game"
        elif int(user_input) > self.number:
            return "Too bad! Your guess was too big - PLEASE RETRY"
        elif int(user_input) < self.number:
            return "Too bad! Your guess was too small - PLEASE RETRY"

    def restart_game(self):
        self.number = random.randrange(1, 21)
        self.counter = 0
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)

    def end_game(self, result):
        if result == "Exiting Game":
            self.root.quit()
        elif result == "Restarting":
            self.restart_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
