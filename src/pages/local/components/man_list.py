from tkinter import Frame, Label, Scrollbar, IntVar, ttk

class ManList:
    def __init__(self, root):
        self.root = root
        self.num_manifests = IntVar(value=0)
        self.tree = None
    
    def update_view(self, entries, num_manifests):
        self.num_manifests.set(num_manifests)
        for entry in entries:
            description = entry[5]
            price = entry[7]
            self.tree.insert('', 'end', text='', values=(description, f'${price}'))
    
    def delete_last_item(self, num_manifests):
        children = self.tree.get_children()
        self.tree.delete(children[len(children) - 1])
        self.num_manifests.set(num_manifests)

    def reset_view(self):
        self.tree.yview_moveto(1)
    
    def build_title(self, f):
        container = Frame(f)
        container.grid(row=0, column=0)

        Label(container, text='Added Manifests:').grid(row=0, column=0)
        Label(container, textvariable=self.num_manifests).grid(row=0, column=1)

    def build_scrollbar(self, root):
        scroll = Scrollbar(root, orient='vertical', command=self.tree.yview)
        scroll.grid(row=1, column=1, sticky='NS')

        self.tree.config(yscrollcommand=scroll.set)
    
    def build_treeview(self, root):
        DEFAULT_COL_WIDTH = 200 # As per Tkinter Treeview docs
        DESC_COL_WIDTH = int(DEFAULT_COL_WIDTH * 1.5)
        PRICE_COL_WIDTH = int(DEFAULT_COL_WIDTH * 0.5)
    
        self.tree = ttk.Treeview(root)

        self.tree['columns'] = ('description', 'price')
        self.tree.column('#0', width=0)
        self.tree.column('description', width=DESC_COL_WIDTH)
        self.tree.column('price', width=PRICE_COL_WIDTH)

        self.tree.heading('description', text='Description', anchor='w')
        self.tree.heading('price', text='Price', anchor='w')
        self.tree.bind('<FocusOut>', lambda e: self.tree.selection_remove(self.tree.focus()))
        
        self.tree.grid(row=1, column=0, sticky='NSEW')

    def build(self):
        f = Frame(self.root)
        f.grid(pady=10)

        self.build_treeview(f)
        self.build_scrollbar(f)
        self.build_title(f)