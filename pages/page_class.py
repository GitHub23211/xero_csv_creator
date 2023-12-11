from tkinter import *

class Page(Frame):
    def __init__(self, state):
        Frame.__init__(self)
        self.state = state
        self.root = state.get_root()
        self.width = 300
        self.height = 700
        self.root.minsize(self.width, self.height)
        self.root.title("Xero Invoice Creator")
        self.grid()