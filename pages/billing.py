from tkinter import Label, Entry, Button

from pages import page

class Billing(page.Page):
    def __init__(self, root, model):
        page.Page.__init__(self, root, model)
        self.prices = self.model.billing['prices']
        self.emps = self.model.billing['emps']
        self.data = {}
    
    def build(self):
        self.grid(row=0, column=0, sticky=('n', 's', 'e', 'w'))
        self.master.columnconfigure(0, weight=1)
        self.columnconfigure([i for i in range(0, 6)], weight=1)
        self.price_cols()
        self.emp_rows()
        self.save_button()
    
    def price_cols(self):
        Label(self, text='EMP').grid(row=0, column=0)
        for i, key in enumerate(self.prices):
            Label(self, text=key).grid(row=0, column=i+1)

    def emp_rows(self):
        for i, name in enumerate(self.emps):
            temp = []
            Label(self, text=self.emps[name]).grid(row=i+1, column=0)
            for j in range(len(self.prices)):
                ent = Entry(self, width=5)
                temp.append(ent)
                ent.grid(row=i+1, column=j+1, padx=2)
            self.data[i] = temp
    
    def save_button(self):
        Button(self, text='Save CSV', command=lambda : self.model.add_bills(self.data)).grid(row=len(self.emps)+1, column=0)