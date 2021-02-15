import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
# Set the font and colours of the text.
tk.Text(root, bg="black", fg="orange", font=("Mono", 8)).pack()
root.geometry("+10+220")  # Position window at left of screen.
root.geometry('150x150')  # Set window size
root.mainloop()
