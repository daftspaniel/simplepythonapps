import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
import os.path
import os

saved_text = ''

# Find the user's home directory and folder where we will save the file.
config_folder = Path.joinpath(Path.joinpath(
    Path.home(), '.config'), 'simplepythonapps')
if not os.path.exists(config_folder):
    os.mkdir(config_folder)
text_file_path = Path.joinpath(config_folder, 'scratchpad.txt')
if not os.path.exists(text_file_path):
    with open(text_file_path, 'x') as f:
        f.write('')
else:
    with open(text_file_path) as f:
        saved_text = f.read()

root = tk.Tk()

# Set the font and colours of the text.
pad = tk.Text(root, bg="black", fg="orange", font=("Mono", 8),
              borderwidth=0)
pad.insert(tk.INSERT, saved_text)

# Call a function when typing occurs on the text box.
pad.bind('<KeyRelease>', lambda *args: pad_text_changed(pad.get("1.0", "end-1c")))
pad.pack()

# Save the text to a file.


def pad_text_changed(text):
    with open(text_file_path, 'w') as f:
        f.write(text)


root.geometry("+10+220")  # Position window at left of screen.

root.geometry('150x150')  # Set window size

# The Escape key closes the application.
root.bind("<Escape>", lambda x: root.destroy())

root.mainloop()
