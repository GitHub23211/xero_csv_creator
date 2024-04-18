from tkinter import Frame, Button

class PricingButtons:
    def __init__(self, root):
        self.root = root
    
    def build(self):
        f = Frame(self.root)#, borderwidth=1, background='red')
        f.grid(row=1, column=1, sticky='N', pady=20)
        Button(f, text='Add Store Pricing', command=self.root.master.nav_add_store).grid(row=1, column=0, sticky='EW')
        Button(f, text='Edit Store Pricing', command=self.root.edit_store).grid(row=2, column=0, sticky='EW')
        Button(f, text='Delete Store Pricing', command=self.root.delete_store).grid(row=3, column=0, sticky='EW')