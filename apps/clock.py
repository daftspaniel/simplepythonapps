# Super simple Tkinter clock. v0.1
import time
import tkinter as tk

from idlelib.tooltip import Hovertip
from datetime import date
from tkutils import buildRootWindow


class App():
    def __init__(self):
        self.root = buildRootWindow()

        # Customise display of time here.
        self.timeLabel = tk.Label(text="", font=(
            "Mono", 18), bg="black", fg="orange")
        self.timeLabel.pack()

        # Put todays date in the tool tip.
        dateTooltip = Hovertip(self.timeLabel, date.today())
        self.root.geometry("+20+20")  # Position Window at top left of screen.

        # The Escape key closes the application.
        self.root.bind("<Escape>", lambda x: self.root.destroy())
        self.update_time()
        self.root.mainloop()

    def update_time(self):
        # Change to "%H:%M" if you don't want seconds.
        self.timeLabel.configure(text=time.strftime("%H:%M:%S"))
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    app = App()
