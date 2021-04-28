"""
    Super simple Tkinter clock. v0.1
"""
import time
import tkinter as tk

from datetime import date
from idlelib.tooltip import Hovertip
from tk_utils import build_root_window

class App: # pylint: disable=too-few-public-methods
    """ Application object for the clock."""
    def __init__(self):
        self.root = build_root_window()

        # Customise display of time here.
        self.time_label = tk.Label(text="", font=(
            "Mono", 18), bg="black", fg="orange")
        self.time_label.pack()

        # Put todays date in the tool tip.
        Hovertip(self.time_label, date.today())
        self.root.geometry("+20+20")  # Position Window at top left of screen.

        # The Escape key closes the application.
        self.root.bind("<Escape>", lambda x: self.root.destroy())
        self.update_time()
        self.root.mainloop()

    def update_time(self):
        """ Display the latest time. """
        # Change to "%H:%M" if you don't want seconds.
        self.time_label.configure(text=time.strftime("%H:%M:%S"))
        self.root.after(1000, self.update_time)


if __name__ == "__main__":
    app = App()
