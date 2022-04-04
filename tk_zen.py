
# Python GUI application that can be created with the use of the built-in tkinter module. 

# This GUI application displays a single Python Zen button. 
# When the button is clicked, the application will open a new window containing the Zen of Python text that was imported from the this module. 
# The this module is a Python easter egg. 
# After import, it prints on standard output the 19 aphorisms that are the guiding principles of Python's design.

# Event-driven programming in GUIs
import this
from tkinter import Tk, Frame, Button, LEFT, messagebox

rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
)

def main_window(root: Tk):
    frame = Frame(root)
    frame.pack()

    zen_button = Button(frame, text="Python Zen", command=show_zen)
    zen_button.pack(side=LEFT)

def show_zen():
    messagebox.showinfo("Zen of Python", this.s.translate(rot13))

if __name__ == "__main__":
    root = Tk()
    main_window(root)
    root.mainloop()


