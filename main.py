import tkinter as tk
import random
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.words = ["apple", "banana", "cherry", "grape", "orange", "kiwi", "melon", "pear", "strawberry", "blueberry"]
        self.current_word = ""
        self.user_input = tk.StringVar()

        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.word_label.pack()

        self.entry = tk.Entry(self.root, textvariable=self.user_input, font=("Helvetica", 18))
        self.entry.pack()

        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test)
        self.start_button.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.result_label.pack()

    def start_test(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.user_input.set("")
        self.entry.config(state="normal")
        self.entry.focus()
        self.start_time = time.time()
        self.start_button.config(state="disabled")

    def check_input(self, event):
        if self.user_input.get() == self.current_word:
            self.entry.config(state="disabled")
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            typing_speed = len(self.current_word) / elapsed_time * 60
            self.result_label.config(text=f"Typing speed: {typing_speed:.2f} words per minute")
            self.start_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    app.entry.bind("<Return>", app.check_input)
    root.mainloop()
