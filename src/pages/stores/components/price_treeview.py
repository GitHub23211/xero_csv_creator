from tkinter import Frame, Scrollbar, ttk

DEFAULT_COL_WIDTH = 200 # As per Tkinter Treeview docs

class PriceTreeView:
    def __init__(self, root):
        self.root = root
        self.tree = None

    def get_tree(self):
        return self.tree
    
    def configure_tree(self, root):
        ID_COL_WIDTH = int(DEFAULT_COL_WIDTH * 0.5)
        NAME_COL_WIDTH = int(DEFAULT_COL_WIDTH * 1)
        PRICE_COL_WIDTH = int(DEFAULT_COL_WIDTH * 0.5)

        tree = ttk.Treeview(root)
        tree['columns'] = ('id', 'name', 'price')
        tree.column('#0', width=0)
        tree.column('id', w=ID_COL_WIDTH)
        tree.column('name', w=NAME_COL_WIDTH)
        tree.column('price', w=PRICE_COL_WIDTH)
        tree.heading('id', text='Store No.', anchor='w')
        tree.heading('name', text='Store Name', anchor='w')
        tree.heading('price', text='Store Pricing', anchor='w')

        self.tree = tree

    def build(self):
        f = Frame(self.root)
        f.grid(rowspan=2)
        self.configure_tree(f)

        scroll = Scrollbar(f, orient='vertical', command=self.tree.yview)
        self.tree.config(yscrollcommand=scroll.set)
        self.tree.config(height=20)
        self.tree.bind('<FocusOut>', lambda e: self.tree.selection_remove(self.tree.focus()))

        scroll.grid(row=0, column=1, sticky='NS')
        self.tree.grid(row=0, column=0, sticky='NSEW')