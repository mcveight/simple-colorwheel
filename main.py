from components.view import gui
import tkinter as tk


def main_loop():
    root = tk.Tk()
    scw = gui(root)
    root.mainloop()


main_loop()
