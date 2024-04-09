from tkinter import Frame, Label, Listbox, Scrollbar, StringVar

class ManList:
    def __init__(self, root):
        self.root = root
        self.man_list = StringVar(value=[])
        self.lbox = None
    
    def set_lbox(self, val):
        self.man_list.set(val)

    def reset_lbox(self):
        self.lbox.yview_moveto(1)

    def build(self):
        f = Frame(self.root)
        f.grid(pady=10)

        Label(f, text='Added Manifests').grid(row=0, column=0)

        self.lbox = Listbox(f, width=55, listvariable=self.man_list, exportselection=0, takefocus=0, selectmode='browse', font=('Segoe UI', 13))
        self.lbox.bind('<FocusOut>', lambda e: self.lbox.selection_clear(0, 'end'))

        scroll = Scrollbar(f, orient='vertical', command=self.lbox.yview)
        self.lbox.configure(yscrollcommand=scroll.set)

        self.lbox.grid(row=1, column=0, sticky='e')
        scroll.grid(row=1, column=1, sticky=('n', 's'))