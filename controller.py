from components.view import gui
import tkinter as tk

class controller:
    def __init__(self, TITLE, GEOMETRY):
        self.root = tk.Tk()
        self.gui = gui(self.root, TITLE, GEOMETRY)
        
        self.main_loop()

    def main_loop(self):
        self.gui.build()
        self.root.mainloop()
