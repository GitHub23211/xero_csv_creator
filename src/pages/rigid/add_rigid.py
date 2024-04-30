from tkinter import Frame, Label, Entry, Button, ttk, StringVar
from .components.header import Header
from .components.items import Items

class AddRigid(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.header = Header(self)
        self.items = Items(self)

    def buttons(self):
        f = Frame(self)
        f.grid(pady=5, sticky='e')

        Button(f, text='Save CSV').grid(sticky='e')

    def build(self):
        self.columnconfigure(0, weight=1)
        self.grid(sticky='we', padx=10)
        self.header.build()
        self.items.build(self.master.pricing, self.master.fuel_levy)
        self.buttons()