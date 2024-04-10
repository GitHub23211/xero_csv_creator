from tkinter import Frame, Label
from .components.list_item import ListItem

class UI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
    
    def build(self):
        self.columnconfigure(0, weight=1)
        self.grid(sticky='EW')
        self.store_list()

    def store_list(self):
        f = Frame(self)
        f.grid(sticky='EW', padx=10, pady=10)

        f.columnconfigure((0, 2, 3, 4), weight=1)
        f.columnconfigure(1, weight=4)

        Label(f, text='Store No.').grid(row=0, column=0)
        Label(f, text='Store Name').grid(row=0, column=1)
        Label(f, text='Store Price').grid(row=0, column=2)
        Label(f, text='Options').grid(row=0, column=3, columnspan=2)

        for i, value in enumerate(self.master.prices.values()):
            ListItem(f, value[0], value[1], value[2], i+1)


