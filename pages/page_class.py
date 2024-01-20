from tkinter import Frame

class Page(Frame):
    def __init__(self, root, model, width, height):
        Frame.__init__(self, root)
        self.root = root
        self.model = model
        root.minsize(width, height)
        root.title("Xero Invoice Creator")