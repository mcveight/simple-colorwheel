import tkinter as tk
from tkinter import Frame, Label
from tkinter.constants import HORIZONTAL, BOTTOM
from .scale import scale
from .square import hsvcolorsquare as square





class colorselector:

    def __init__(self, root):

        
        self.root = root

        self.values = {
                "h": tk.IntVar(),
                "s": tk.IntVar(),
                "l": tk.IntVar(),
                "hex": tk.IntVar()
                }

        self.hex_textbox = tk.Entry(
                self.root, width=8,
                bg="white", fg="black" )


        self.frame = Frame(self.root)
        self.square = square(self.frame)
        self.H_scale = scale(self.frame, 0, 360, 120, function = self.scaleMove)
        self.S_scale = scale(self.frame, 0, 100, 120, function = self.scaleMove)
        self.L_scale = scale(self.frame, 0, 100, 120, function = self.scaleMove)

    def scaleMove(self,*args):
        self.values["h"] = int( self.H_scale.object.get() )
        self.values["s"] = int( self.S_scale.object.get() )
        self.values["l"] = int( self.L_scale.object.get() )


        '''
        self.hex_entry.delete(0,tk.END)
        self.hex_entry.insert(0,self.hex)
        '''


    def build(self):
        self.frame.pack( )
        self.square.object.pack( )
        self.H_scale.object.pack( )
        self.S_scale.object.pack( )
        self.L_scale.object.pack( )
