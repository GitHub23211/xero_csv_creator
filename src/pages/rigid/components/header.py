from tkinter import Frame, Label, Entry, Button, StringVar

class Header(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.date = StringVar(value='')
        self.inv_num = StringVar(value='')
        self.fuel_levy = StringVar(value='')

    def get_date(self):
        return self.date.get()
    
    def get_inv_num(self):
        return self.inv_num.get()
    
    def get_fuel_levy(self):
        return self.fuel_levy.get()

    def build(self):
        self.columnconfigure(list(range(7)), weight=1)
        self.grid(sticky='we', pady=10)

        Label(self, text='Invoice Start Date').grid(row=0, column=0)
        Entry(self, textvariable=self.date).grid(row=0, column=1)

        Label(self, text='Invoice No.').grid(row=0, column=2)
        Entry(self, textvariable=self.inv_num).grid(row=0, column=3)

        Label(self, text='Fuel Levy').grid(row=0, column=4)
        Entry(self, textvariable=self.fuel_levy).grid(row=0, column=5)

        Label(self, text='%').grid(row=0, column=6)