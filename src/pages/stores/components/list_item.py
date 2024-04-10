from tkinter import Frame, Label, Button

class ListItem:
    def __init__(self, root, num, name, price, row):
        self.root = root
        self.row = row
        self.store_num = num
        self.store_name = name
        self.store_price = price
        self.build()
    
    def build(self):
        Label(self.root, text=self.store_num).grid(row=self.row, column=0)
        Label(self.root, text=self.store_name).grid(row=self.row, column=1)
        Label(self.root, text=f'${self.store_price}').grid(row=self.row, column=2)

        Button(self.root, text='Edit', command=lambda: print('Edit store')).grid(row=self.row, column=3, sticky=('WE'))
        Button(self.root, text='Delete', command=lambda: print('Delete store')).grid(row=self.row, column=4, sticky=('WE'))
