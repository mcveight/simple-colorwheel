from .component import tk

class text:
    def __init__(self, parent):

        self.object = tk.Text(
                parent, bd = 0,
                bg='#fff', fg= '#000',
                width=100)

        self.object.set(0)
