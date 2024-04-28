from tkinter import Frame, Label, Entry, Button, ttk, StringVar

class AddRigid(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
    
    def show_date(self):
        f = Frame(self)
        f.columnconfigure(list(range(7)), weight=1)
        f.grid(sticky='we', pady=10)

        Label(f, text='Invoice Start Date').grid(row=0, column=0)
        Entry(f).grid(row=0, column=1)

        Label(f, text='Invoice No.').grid(row=0, column=2)
        Entry(f).grid(row=0, column=3)

        Label(f, text='Fuel Levy').grid(row=0, column=4)
        Entry(f).grid(row=0, column=5)
        Label(f, text='%').grid(row=0, column=6)

    def show_item_line(self):
        f = Frame(self)
        f.columnconfigure(list(range(2)), weight=1)
        f.grid(sticky='we')

        i = 1

        Label(f, text='Inventory Code').grid(row=i, column=0)
        Label(f, text='Description').grid(row=i, column=1)
        Label(f, text='Quantity').grid(row=i, column=2)
        Label(f, text='Total Amount').grid(row=i, column=3)
        ttk.Separator(f, orient='horizontal').grid(row=i+1, column=0, columnspan=4, sticky='ew', pady=5)

        i = i + 2
  
        for k, v in self.master.pricing.items():
            self.generate_item_line(k, v, f, i)
            i = i + 2
    
    def generate_item_line(self, k, v, f, i):
        code = v[1]
        date = '11/2'
        if 'ST' in k:
            description = f'{date} (Sunday) - UNIT PRICE ${v[2]} + FL {self.master.fuel_levy * 100}%'
        else: 
            description = f'UNIT PRICE ${v[2]} + FL {self.master.fuel_levy * 100}%'
        
        Label(f, text=code).grid(row=i, column=0, sticky='we')
        Label(f, text=description).grid(row=i, column=1, sticky='we')
        Entry(f).grid(row=i, column=2)
        Label(f, text='$6481').grid(row=i, column=3)
        ttk.Separator(f, orient='horizontal').grid(row=i+1, column=0, columnspan=4, sticky='ew', pady=5)

    def buttons(self):
        f = Frame(self)
        f.grid(pady=5, sticky='e')

        Button(f, text='Save CSV').grid(sticky='e')

    def build(self):
        self.columnconfigure(0, weight=1)
        self.grid(sticky='we', padx=10)
        self.show_date()
        self.show_item_line()
        self.buttons()