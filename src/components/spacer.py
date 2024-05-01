from tkinter import Frame

class Spacer(Frame):
    def __init__(self, root, height):
        Frame.__init__(self, root)
        self.grid(pady=height)