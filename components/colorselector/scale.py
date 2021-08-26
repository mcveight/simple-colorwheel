from .component import tk, HORIZONTAL




class scale:
    def __init__(self, parent, from_,
            to_, length_, fg_ = "#FFFFFF", function = None,
            label_=''):

        self.object = tk.Scale(
                parent, from_= from_,
                to= to_, length= length_,
                fg = fg_, orient= HORIZONTAL,
                command= function, label= label_)

        self.object.set(0)
