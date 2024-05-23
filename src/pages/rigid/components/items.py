from tkinter import Frame, Label, Entry, Button, ttk, StringVar, IntVar, DoubleVar
from .header import Header
from .spacer import Spacer

class Items(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.fuel_levy = DoubleVar(value=0.0)
        self.header = Header(root, self.fuel_levy)
        self.pricing = None
        self.total_amounts = {}

    def get_stores(self):
        return self.total_amounts

    def show_item_line(self):
        i = 1
        Label(self, text='Inventory Code').grid(row=i, column=0)
        Label(self, text='Description').grid(row=i, column=1)
        Label(self, text='Adjusted Price').grid(row=i, column=2)
        Label(self, text='Quantity').grid(row=i, column=3)
        ttk.Separator(self, orient='horizontal').grid(row=i+1, column=0, columnspan=4, sticky='ew', pady=5)

        i = i + 2
        for k, v in self.pricing:
            self.generate_item_line(k, v, i)
            i = i + 2
    
    def generate_item_line(self, k, v, i):
        code = v[1]
        date = '11/2'
        levy = self.fuel_levy.get()
        unit_price = v[2]
        adjusted_price = "%.2f" % (unit_price * (1+(levy/100)))
        if 'ST' in k:
            description = f'{date} (Sunday) - UNIT PRICE ${unit_price} + FL {levy}%'
        elif '114' in k:
            description = f'UNIT PRICE ${unit_price}'
            adjusted_price = unit_price
        else: 
            description = f'UNIT PRICE ${unit_price} + FL {levy}%'
        
        Label(self, text=code).grid(row=i, column=0, sticky='we')
        Label(self, text=description).grid(row=i, column=1, sticky='we')
        Label(self, text=f'${adjusted_price}').grid(row=i, column=2, sticky='we')
        quantity = Entry(self)
        quantity.grid(row=i, column=3)
        ttk.Separator(self, orient='horizontal').grid(row=i+1, column=0, columnspan=4, sticky='ew', pady=5)

        self.total_amounts[k] = {
            'code': code,
            'description': description,
            'price': adjusted_price,
            'quantity': quantity
        }
    
    def build(self, pricing, fuel_levy):
        self.pricing = pricing
        self.fuel_levy.set(fuel_levy*100)
        self.columnconfigure(1, weight=10)
        self.columnconfigure([0, 2], weight=1)

        self.header.build()
        Spacer(self, height=5)
        self.grid(sticky='we')
        self.show_item_line()
        Spacer(self, height=5)