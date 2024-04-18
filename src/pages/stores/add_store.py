from tkinter import Frame, Label, Entry, Button, StringVar, messagebox

class AddStore(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.store_num_var = StringVar(value='')
        self.store_name_var = StringVar(value='')
        self.store_price_var = StringVar(value='')
    
    def save_details(self):
        try:
            key = self.store_num_var.get()
            new_store = [
                    int(key),
                    self.store_name_var.get(),
                    self.store_price_var.get()
                ]
            self.master.add_new_store(key, new_store)
        except Exception as e:
            messagebox.showerror('Error', e)
            self.focus()
    
    def buttons(self):
        f = Frame(self)
        f.columnconfigure(0, weight=1)
        f.grid(pady=10, sticky='EW')

        Button(f, text='Save', command=self.save_details).grid(sticky='EW')
        Button(f, text='Back', command=self.master.nav_store_list).grid(sticky='EW', pady=5)

    def build(self):
        self.grid(pady=20)
        f = Frame(self)
        f.grid()
        Label(f, text='Store No.').grid(row=0, column=0)
        Label(f, text='Store Name').grid(row=1, column=0, pady=10)
        Label(f, text='Store Pricing').grid(row=2, column=0)
        
        Entry(f, textvariable=self.store_num_var).grid(row=0, column=1)
        Entry(f, textvariable=self.store_name_var).grid(row=1, column=1, pady=10)
        Entry(f, textvariable=self.store_price_var).grid(row=2, column=1)

        self.buttons()