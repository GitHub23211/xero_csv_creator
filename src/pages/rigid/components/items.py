from tkinter import Frame, Label, Entry, Button, ttk, StringVar

class Items(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.pricing = None
        self.fuel_levy = None
    
    def show_item_line(self):
        self.columnconfigure(list(range(2)), weight=1)
        self.grid(sticky='we')

        i = 1
        Label(self, text='Inventory Code').grid(row=i, column=0)
        Label(self, text='Description').grid(row=i, column=1)
        Label(self, text='Quantity').grid(row=i, column=2)
        Label(self, text='Total Amount').grid(row=i, column=3)
        ttk.Separator(self, orient='horizontal').grid(row=i+1, column=0, columnspan=4, sticky='ew', pady=5)

        i = i + 2
        for k, v in self.pricing:
            self.generate_item_line(k, v, i)
            i = i + 2
    
    def generate_item_line(self, k, v, i):
        code = v[1]
        date = '11/2'
        if 'ST' in k:
            description = f'{date} (Sunday) - UNIT PRICE ${v[2]} + FL {self.fuel_levy * 100}%'
        else: 
            description = f'UNIT PRICE ${v[2]} + FL {self.fuel_levy * 100}%'
        
        Label(self, text=code).grid(row=i, column=0, sticky='we')
        Label(self, text=description).grid(row=i, column=1, sticky='we')
        Entry(self).grid(row=i, column=2)
        Label(self, text='$6481').grid(row=i, column=3)
        ttk.Separator(self, orient='horizontal').grid(row=i+1, column=0, columnspan=4, sticky='ew', pady=5)
    
    def build(self, pricing, fuel_levy):
        self.pricing = pricing
        self.fuel_levy = fuel_levy
        self.show_item_line()