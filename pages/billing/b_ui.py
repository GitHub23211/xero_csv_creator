from tkinter import Frame, Label, Entry, Button

class billingUI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

    def build(self):
        self.grid(row=0, column=0, sticky=('n', 's', 'e', 'w'))
        self.master.columnconfigure(0, weight=1)
        self.columnconfigure([i for i in range(0, 6)], weight=1)
        self.grid()
        self.date()
        self.price_cols()
        self.emp_rows()
        self.save_button()
    
    def date(self):
        f = Frame(self)
        f.grid(row=0, column=0, padx=10)
        Label(f, text='Start Work Date (dd/mm/yy)').grid(row=0, column=0)
        Entry(f, textvariable=self.master.date_var).grid(row=0, column=1)
    
    def price_cols(self):
        f = Frame(self)
        f.grid(row=1, column=0)
        Label(self, text='EMP').grid(row=1, column=0)
        for i, key in enumerate(self.master.prices):
            Label(self, text=key).grid(row=1, column=i+1)

    def emp_rows(self):
        f = Frame(self)
        f.grid(row=2, column=0)
        for i, name in enumerate(self.master.emps):
            temp = {}
            Label(self, text=self.master.emps[name][1]).grid(row=i+2, column=0, sticky=('w', 'e'))
            for j, price in enumerate(self.master.prices):
                ent = Entry(self, width=5)
                temp[price] = ent
                ent.grid(row=i+2, column=j+1, padx=2)
            self.master.data[name] = temp

    def save_button(self):
        Button(self, text='Save CSV', command=self.master.submit).grid(row=len(self.master.emps)+2, column=0, pady=10)