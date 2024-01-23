from tkinter import Frame

class Page(Frame):
    def __init__(self, root, model):
        Frame.__init__(self, root)
        self.model = model