from tkinter import Frame, Entry, Label, StringVar

class ManInfoInput:
    def __init__(self, root):
        self.root = root
        self.man_num_var = StringVar(value='')
        self.man_date_var = StringVar(value='')
        self.man_num_ent = None
    
    def get_man_num(self):
        return self.man_num_var.get()

    def get_man_date(self):
        return self.man_date_var.get()

    def set_man_date(self, date):
        self.man_date_var.set(date)
    
    def reset_man_num(self):
        self.man_num_var.set('')
    
    def return_focus(self):
        self.man_num_ent.focus()

    def build(self):
        f = Frame(self.root)
        f.grid()

        Label(master=f, text='Manifest Date').grid(row=0, column=0)
        Label(master=f, text='Manifest Number').grid(row=0, column=1)
        Entry(master=f, textvariable=self.man_date_var).grid(row=1, column=0, padx=5)

        self.man_num_ent = Entry(master=f, textvariable=self.man_num_var)
        self.man_num_ent.grid(row=1, column=1, padx=5)
        self.man_num_ent.focus()