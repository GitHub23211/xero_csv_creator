from tkinter import *

class Page(Frame):
    def __init__(self, state, width, height):
        Frame.__init__(self)
        self.state = state
        self.root = state.root
        self.model = state.model
        self.width = width
        self.height = height
        self.root.minsize(self.width, self.height)
        self.root.title("Xero Invoice Creator")
        self.grid()