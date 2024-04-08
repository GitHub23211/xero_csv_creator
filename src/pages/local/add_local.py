from tkinter import Frame, Entry, Button, Label, Listbox, Scrollbar, Checkbutton

class AddLocal(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.man_num_ent = None
        self.lbox = None
    
    def build(self):
        self.grid()
        self.manifest_input()
        self.store_input()
        self.added_manifests()
        self.master.bind('<Return>', self.add_manifest)

    def manifest_input(self):
        f = Frame(self)
        f.grid(row=0, column=0)

        Label(master=f, text='Manifest Date').grid(row=0, column=0)
        Label(master=f, text='Manifest Number').grid(row=0, column=1)
        Entry(master=f, textvariable=self.master.man_date_var).grid(row=1, column=0, padx=5)

        self.man_num_ent = Entry(master=f, textvariable=self.master.man_num_var)
        self.man_num_ent.grid(row=1, column=1, padx=5)
        self.man_num_ent.focus()

    def store_input(self):
        f = Frame(self)
        f.grid(row=1, column=0)

        loaded_checkbox = Checkbutton(f, text='Loaded by driver?', variable=self.master.loaded, takefocus=0)
        loaded_checkbox.grid(row=0, column=1)

        Label(f, text="Store Number").grid(row=1, column=0)

        for i in range(2, 5):
            str_no_ent = Entry(f)
            str_no_ent.grid(row=i, column=0)
            self.master.stores_nums.append(str_no_ent)
        
        add_ent_btn = Button(f, text="Add Manifest", command=self.add_manifest, takefocus=0)
        add_ent_btn.grid(row=2, column=1, padx=20, sticky=('e', 'w'))

        del_ent_btn = Button(f, text="Delete Last Entry", command=self.master.delete_manifest, takefocus=0)
        del_ent_btn.grid(row=3, column=1, padx=20, sticky=('e', 'w'))

        save_csv_btn = Button(f, text='Save CSV', command=self.master.save_csv, takefocus=0)
        save_csv_btn.grid(row=4, column=1, padx=20, sticky=('e', 'w'))

    def added_manifests(self):
        f = Frame(self)
        f.grid(row=2, column=0, pady=10)

        Label(f, text='Added Manifests').grid(row=0, column=0)

        self.lbox = Listbox(f, width=55, listvariable=self.master.man_list, exportselection=0, takefocus=0, selectmode='browse', font=('Segoe UI', 13))
        self.lbox.bind('<FocusOut>', lambda e: self.lbox.selection_clear(0, 'end'))

        scroll = Scrollbar(f, orient='vertical', command=self.lbox.yview)
        self.lbox.configure(yscrollcommand=scroll.set)

        self.lbox.grid(row=1, column=0, sticky='e')
        scroll.grid(row=1, column=1, sticky=('n', 's'))
    
    def add_manifest(self, event=None):
        self.master.add_manifest()
        self.man_num_ent.focus()
        self.lbox.yview_moveto(1)