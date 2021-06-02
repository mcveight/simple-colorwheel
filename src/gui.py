import tkinter as tk

class gui():
    
    def __init__(self, root):
        super().__init__()

        self.root = root
        
        self.sq_primary_color = 0

        self.sq_secondary_color = 0

        self.hex_textbox = tk.Entry(self.root, width=8, 
                                    bg="white", fg="black" )

        self.initUI()

    def initUI(self):
        
        # initialize modules


        self.root.title("swc 0.01b")

        frame_colours = tk.Frame(self.root, padx = 0, pady = 0,
                                cursor = "hand2", bd = 2)
         
        self.hex_textbox = tk.Entry(self.root, width=8, 
                                    bg="white", fg="black" )

        self.sq_primary_color = tk.Canvas(self.root, bg="#000000")

        self.sq_secondary_color = tk.Canvas(self.root, bg="#000000");


       
        # grid positioning 
        '''
        frame_colours.grid(row=0)

        self.sq_primary_color.grid(row=0,sticky=tk.E)

        self.sq_secondary_color.grid(row=0, column=1, sticky=tk.W)
        '''
        self.hex_textbox.grid(row=0, column=1, columnspan=3,
                              padx=10, pady=10)


    def update_colour(oldColor: hex, oldBox, newBox):
        pass

