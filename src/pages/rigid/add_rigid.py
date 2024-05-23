from tkinter import Frame, Label, Entry, Button, ttk, StringVar
from .components.items import Items
from .components.spacer import Spacer

class AddRigid(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.items = Items(self)

    def buttons(self):
        f = Frame(self)
        f.columnconfigure(0, weight=1)
        f.grid(sticky='we')
        Button(f, text='Save CSV', command=self.save_csv).grid(sticky='we')

    def build(self):
        self.columnconfigure(0, weight=1)
        self.grid(sticky='we', padx=10)
        Spacer(root=self, height=5)
        self.items.build(self.master.pricing, self.master.fuel_levy)
        self.buttons()
        Spacer(root=self, height=8)
    
    def save_csv(self):
        inv_date = self.items.header.get_date()
        inv_num = self.items.header.get_inv_num()
        rigid_stores = self.items.get_stores()
        invoice = self.master.invoice.create_rigid_invoice(inv_date, inv_num, rigid_stores)
        self.master.save_csv(invoice)