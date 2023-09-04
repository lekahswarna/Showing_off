import tkinter as tk

def clear_text():
    text.delete(1.0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Text Disappearing App")

# Create a Text widget for typing text
text = tk.Text(window, height=10, width=40)
text.pack()

# Create a button to clear the text
clear_button = tk.Button(window, text="Clear Text", command=clear_text)
clear_button.pack()

# Start the main loop
window.mainloop()
