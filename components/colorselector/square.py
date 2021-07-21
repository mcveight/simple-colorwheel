from .component import tk, Label




class hsvcolorsquare:
    def __init__(self, parent):
        self.object = Label(
                parent, bg= "#000000",width= 6,
                height= 3,bd = 1
                )

        # ease the action of update_color
        self.parent = parent

    def update_color(self, hexval):
        self.parent.clipboard_clear()
        self.parent.clipboard_append(hexval)
