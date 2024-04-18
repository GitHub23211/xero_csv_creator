from tkinter import Frame, Label, Button, Entry

class SearchBar:
    def __init__(self, root):
        self.root = root

    def build(self):
        f = Frame(self.root)#, borderwidth=1, background='green')
        f.grid(row=0, column=1, padx=20, sticky='S')

        search_bar_ent = Entry(f, textvariable=self.root.search_term)
        search_bar_ent.bind('<Return>', lambda e: self.root.search_stores())

        Label(f, text='Search by Store No.').grid(columnspan=2)
        search_bar_ent.grid(columnspan=2)
        Button(f, text='Search', command=self.root.search_stores).grid(row=2, column=0, sticky='EW')
        Button(f, text='Reset', command=self.root.reset_stores).grid(row=2, column=1, sticky='EW')