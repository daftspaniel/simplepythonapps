import tkinter as tk

# Create a simple window with no icon or text shown in title bar.
def buildRootWindow():
    root = tk.Tk()        
    icon = tk.PhotoImage(height=16, width=16)
    icon.blank()
    root.wm_iconphoto('True', icon)
    root.title('')
    return root