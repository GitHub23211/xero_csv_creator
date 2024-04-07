from tkinter import Frame, Entry, Button, Label, Listbox, Scrollbar, Checkbutton

class AddLocal(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
    
    def build(self):
        self.grid()
        self.manifest_input()
        self.store_input()
        self.added_manifests()
        self.master.man_num_ent.focus()

    def manifest_input(self):
        frame = Frame(self)
        frame.grid(row=0, column=0)

        Label(master=frame, text='Manifest Date').grid(row=0, column=0)
        Label(master=frame, text='Manifest Number').grid(row=0, column=1)

        self.master.man_date_ent = Entry(master=frame)
        self.master.man_date_ent.grid(row=1, column=0, padx=5)
        self.master.man_date_ent.insert(0, self.master.get_inv_date())

        self.master.man_num_ent = Entry(master=frame)
        self.master.man_num_ent.grid(row=1, column=1, padx=5)

    def store_input(self):
        frame = Frame(self)
        frame.grid(row=1, column=0)

        self.master.loaded_checkbox_widget = Checkbutton(frame, text='Loaded by driver?', variable=self.master.loaded, takefocus=0)
        self.master.loaded_checkbox_widget.grid(row=0, column=1)

        Label(frame, text="Store Number").grid(row=1, column=0)

        for i in range(2, 5):
            str_no_ent = Entry(frame)
            str_no_ent.grid(row=i, column=0)
            self.master.stores_nums.append(str_no_ent)
        
        add_ent_btn = Button(frame, text="Add Manifest", command=self.master.add_manifest, takefocus=0)
        add_ent_btn.grid(row=2, column=1, padx=20, sticky=('e', 'w'))

        del_ent_btn = Button(frame, text="Delete Last Entry", command=self.master.delete_manifest, takefocus=0)
        del_ent_btn.grid(row=3, column=1, padx=20, sticky=('e', 'w'))

        save_csv_btn = Button(frame, text='Save CSV', command=self.master.save_csv, takefocus=0)
        save_csv_btn.grid(row=4, column=1, padx=20, sticky=('e', 'w'))

        self.master.bind('<Return>', self.master.add_manifest)

    def added_manifests(self):
        frame = Frame(self)
        frame.grid(row=2, column=0, pady=10)

        Label(frame, text='Added Manifests').grid(row=0, column=0)

        self.master.lbox = Listbox(frame, width=55, listvariable=self.master.man_var, exportselection=0, takefocus=0, selectmode='browse', font=('Segoe UI', 13))
        self.master.lbox.bind('<FocusOut>', lambda e: self.master.lbox.selection_clear(0, 'end'))

        scroll = Scrollbar(frame, orient='vertical', command=self.master.lbox.yview)
        self.master.lbox.configure(yscrollcommand=scroll.set)

        self.master.lbox.grid(row=1, column=0, sticky='e')
        scroll.grid(row=1, column=1, sticky=('n', 's'))