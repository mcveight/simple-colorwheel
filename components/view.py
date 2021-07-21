import tkinter as tk
from .colorselector.component import colorselector  as colselec
class gui():
    
    def __init__(self, root, TITLE, GEOMETRY):
        super().__init__()
        
        # root window settings
        self.root = root
        self.root.title(TITLE)
        self.root.geometry(GEOMETRY)


        # unresizable root window
        self.root.resizable(0, 0)

        #init components

        self.colselec = colselec(self.root)


    def build(self):
        self.colselec.build()
