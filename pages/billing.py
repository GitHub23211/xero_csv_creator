from tkinter import Frame, Label, Entry, Button, StringVar, messagebox

from pages import page

class Billing(page.Page):
    def __init__(self, root, model):
        page.Page.__init__(self, root, model)
        self.prices = self.model.billing['prices']
        self.emps = self.model.billing['emps']
        self.date_var = StringVar(value='')
        self.data = {}
    
    def build(self):
        self.grid(row=0, column=0, sticky=('n', 's', 'e', 'w'))
        self.master.columnconfigure(0, weight=1)
        self.columnconfigure([i for i in range(0, 6)], weight=1)
        self.date()
        self.price_cols()
        self.emp_rows()
        self.save_button()
    
    def date(self):
        f = Frame(self)
        f.grid(row=0, column=0, padx=10, pady=10)
        Label(f, text='Start Work Date').grid(row=0, column=0)
        Entry(f, textvariable=self.date_var).grid(row=0, column=1)

    
    def price_cols(self):
        f = Frame(self)
        f.grid(row=1, column=0, padx=10)
        Label(self, text='EMP').grid(row=1, column=0)
        for i, key in enumerate(self.prices):
            Label(self, text=key).grid(row=1, column=i+1)

    def emp_rows(self):
        f = Frame(self)
        f.grid(row=2, column=0, padx=10)
        for i, name in enumerate(self.emps):
            temp = {}
            Label(self, text=self.emps[name]).grid(row=i+2, column=0)
            for j, price in enumerate(self.prices):
                ent = Entry(self, width=5)
                temp[price] = ent
                ent.grid(row=i+2, column=j+1, padx=2)
            self.data[name] = temp
    
    def submit(self):
        try:
            self.model.add_bills(self.data, self.date_var.get())
        except Exception as e:
            messagebox.showerror('Error', f'Store number {e} does not exist')

    def save_button(self):
        Button(self, text='Save CSV', command=self.submit).grid(row=len(self.emps)+2, column=0, padx=10)