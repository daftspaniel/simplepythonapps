# Super simple Tkinter clock. v0.1
# Public domain.
# 2021 Feb 13 - daftspaniel - www.casterbridge.xyz

import tkinter as tk
from idlelib.tooltip import Hovertip

import time
from datetime import date


class App():
    def __init__(self):
        self.root = tk.Tk()

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


app = App()