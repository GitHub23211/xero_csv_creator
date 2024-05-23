from tkinter import Frame, Label, Entry, Button, StringVar

class Header(Frame):
    def __init__(self, root, fuel_levy):
        Frame.__init__(self, root)
        self.date = StringVar(value='')
        self.inv_num = StringVar(value='')
        self.fuel_levy = fuel_levy

    def get_date(self):
        return self.date.get()
    
    def get_inv_num(self):
        return self.inv_num.get()

    def build(self):
        self.columnconfigure(list(range(3)), weight=1)
        self.grid(sticky='we')

        Label(self, text='Invoice Start Date').grid(row=0, column=0)
        Entry(self, textvariable=self.date).grid(row=1, column=0)

        Label(self, text='Invoice No.').grid(row=0, column=1)
        Entry(self, textvariable=self.inv_num).grid(row=1, column=1)

        Label(self, text='Fuel Levy (%)').grid(row=0, column=2)
        fl = Entry(self, textvariable=self.fuel_levy)
        fl.grid(row=1, column=2)