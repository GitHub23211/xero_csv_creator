from tkinter import Frame, Entry, Button, Label, StringVar, Listbox, Scrollbar, messagebox

from pages import page_class

class AddManifest(page_class.Page):
    def __init__(self, state):
        page_class.Page.__init__(self, state, 270, 350)
        self.man_var = StringVar(value=[])
        self.man_date_ent = None
        self.man_num_ent = None
        self.lbox = None
        self.lbox_index = -1
        self.load_info = []
        self.manifest_input()
        self.store_input()
        self.added_manifests()
        self.man_num_ent.focus()

    def manifest_input(self):
        frame = Frame(self)
        frame.grid(row=0, column=0)

        man_date_lbl = Label(master=frame, text='Manifest Date')
        man_date_lbl.grid(row=0, column=0)

        man_num_lbl = Label(master=frame, text='Manifest Number')
        man_num_lbl.grid(row=0, column=1)

        self.man_date_ent = Entry(master=frame)
        self.man_date_ent.insert(0, self.model.inv_date)
        self.man_date_ent.grid(row=1, column=0, padx=5)

        self.man_num_ent = Entry(master=frame)
        self.man_num_ent.grid(row=1, column=1, padx=5)

    def store_input(self):
        frame = Frame(self)
        frame.grid(row=1, column=0)

        str_num_lbl = Label(frame, text="Store Number")
        str_num_lbl.grid(row=0, column=0)

        for i in range(1, 4):
            str_no_ent = Entry(frame)
            str_no_ent.grid(row=i, column=0)
            self.load_info.append(str_no_ent)
        
        def buttons():
            add_ent_btn = Button(frame, text="Add Manifest", command=self.append_manifest, takefocus=0)
            add_ent_btn.grid(row=1, column=1, padx=20, sticky=('e', 'w'))

            del_ent_btn = Button(frame, text="Delete Last Entry", command=self.delete_manifest, takefocus=0)
            del_ent_btn.grid(row=2, column=1, padx=20, sticky=('e', 'w'))

            save_csv_btn = Button(frame, text='Save CSV', command=self.model.save_csv, takefocus=0)
            save_csv_btn.grid(row=3, column=1, padx=20, sticky=('e', 'w'))

        self.root.bind('<Return>', self.append_manifest)
        buttons()   

    def added_manifests(self):
        frame = Frame(self)
        frame.grid(row=2, column=0, pady=10)

        title_lbl = Label(frame, text='Added Manifests')
        title_lbl.grid(row=0, column=0)

        self.lbox = Listbox(frame, width=50, listvariable=self.man_var, exportselection=0, takefocus=0, selectmode='extended')
        self.lbox.bind('<<ListboxSelect>>', self.update_lbox_index)

        scroll = Scrollbar(frame, orient='vertical', command=self.lbox.yview)
        self.lbox.configure(yscrollcommand=scroll.set)

        self.lbox.grid(row=1, column=0, sticky='e')
        scroll.grid(row=1, column=1, sticky=('n', 's'))

    def append_manifest(self, event=None):
        try:
            self.update_added_manifests(self.man_date_ent.get(), self.man_num_ent.get())
            for i in range(0, 3):
                self.load_info[i].delete(0, 'end')
            self.man_num_ent.delete(0, 'end')
            self.lbox.select_clear('active', 'end')
            self.lbox_index = -1
            self.lbox.yview_moveto(1)
            self.man_num_ent.focus()
        except Exception as e:
            messagebox.showerror('Error', f'Store number {e} does not exist')

    def update_lbox_index(self, event=None):
        if self.lbox.curselection()[0] == self.lbox_index - 2:
            self.lbox.select_clear('active', 'end')
            self.lbox_index = -1
        else:
            self.lbox_index = -1 if len(self.lbox.curselection()) == 0 else self.lbox.curselection()[0] + 2
        
    def update_added_manifests(self, date, num):
        self.model.add_manifest(self.load_info, date, num, self.lbox_index)
        manifests = self.model.manifests
        show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
        self.man_var.set(show_manifests)

    def delete_manifest(self):
        manifests = self.model.manifests
        if len(manifests) > 1:
            manifests.pop()
            show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
            self.man_var.set(show_manifests)

