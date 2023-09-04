import tkinter as tk
from tkinter import ttk

def fade_text():
    for alpha in range(255, 0, -10):
        text_label.configure(foreground=f'#{alpha:02x}{alpha:02x}{alpha:02x}')
        root.update()
        root.after(100)  # Delay in milliseconds

root = tk.Tk()
root.title("Disappearing Text")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

text_label = ttk.Label(frame, text="Text will disappear when you click the button.")
text_label.pack(padx=10, pady=10)

fade_button = ttk.Button(frame, text="Fade Text", command=fade_text)
fade_button.pack(padx=10, pady=10)

root.mainloop()
