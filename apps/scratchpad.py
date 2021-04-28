"""
    Super simple Tkinter clock. v0.1
"""
import os
import os.path
import tkinter as tk
from pathlib import Path

from tk_utils import build_root_window


class App():
    """ Application object for the scratchpad."""

    def __init__(self):
        self.root = build_root_window()

        # Set the font and colours of the text.
        self.pad = tk.Text(self.root, bg="black", fg="orange",
                           font=("Mono", 8),
                           borderwidth=0)
        # Set the pad to show the saved text.
        self.pad.insert(tk.INSERT, self.load_saved_text())
        self.pad.pack()

        # Call a function when typing occurs on the text box.
        def key_press_handler(*args):# pylint: disable=unused-argument
            self.pad_text_changed(self.pad.get("1.0", "end-1c"))
        self.pad.bind('<KeyRelease>', key_press_handler)

        # The Escape key closes the application.
        self.root.bind("<Escape>", lambda x: self.root.destroy())

        self.root.geometry("+10+220")  # Position window at left of screen.
        self.root.geometry('150x150')  # Set window size
        self.root.mainloop()

    def load_saved_text(self):
        """
            Retrieve the stored text file.
        """
        # Find the user's home directory and folder
        # where we will save the file.
        config_folder = Path.joinpath(Path.joinpath(
            Path.home(), '.config'), 'simplepythonapps')
        # Create config folder if it does not exist
        if not os.path.exists(config_folder):
            os.mkdir(config_folder)
        # Build path to our text file.
        self.text_file_path = Path.joinpath(config_folder, 'scratchpad.txt')

        # Create new file or read text from existing file.
        if not os.path.exists(self.text_file_path):
            with open(self.text_file_path, 'x') as text_file:
                text_file.write('')
                return ''
        else:
            with open(self.text_file_path) as text_file:
                return text_file.read()

    def pad_text_changed(self, text):
        """
            When the text changes, save it to the file.
        """
        with open(self.text_file_path, 'w') as text_file:
            text_file.write(text)


if __name__ == "__main__":
    app = App()
