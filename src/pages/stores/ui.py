from tkinter import Frame, Label, Scrollbar, ttk
from .components.list_item import ListItem

class UI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
    
    def build(self):
        self.columnconfigure(0, weight=1)
        self.grid(sticky='EW')
        self.store_list()

    def store_list(self):
        tree = ttk.Treeview(self)

        tree['columns'] = ('id', 'name', 'price')
        tree.column('#0', width=0)
        tree.heading('id', text='Store No.', anchor='w')
        tree.heading('name', text='Store Name', anchor='w')
        tree.heading('price', text='Store Pricing', anchor='w')

        for values in self.master.prices.values():
            tree.insert('', 'end', text='', values=(values[0], values[1], f'${values[2]}'))
        
        scroll = Scrollbar(self, orient='vertical', command=tree.yview)
        tree.config(yscrollcommand=scroll.set)
        tree.config(height=20)

        scroll.grid(row=0, column=1, sticky='NS')
        tree.grid(row=0, column=0, sticky='NSEW')

