from tkinter import *

from pages import page_class

class AddManifest(page_class.Page):
    def __init__(self, state):
        page_class.Page.__init__(self, state, 300, 700)
        self.man_var = StringVar(value=[])
        self.manifest_info()
        self.added_manifests()

    def manifest_info(self):
        frame = Frame(self.root)
        frame.grid(row=0, column=0)

        man_date_lbl = Label(master=frame, text="Manifest Date")
        man_no_lbl = Label(master=frame, text="Manifest Number")

        man_date_lbl.grid(row=0, column=0)
        man_no_lbl.grid(row=0, column=1)

        man_date_ent = Entry(master=frame)
        man_no_ent = Entry(master=frame)
        man_date_ent.grid(row=1, column=0)
        man_no_ent.grid(row=1, column=1)

        str_no_lbl = Label(master=frame, text="Store Number")
        str_no_lbl.grid(row=2, column=0)

        load_info = []
        for i in range(4, 7):
            str_no_ent = Entry(master=frame)
            str_no_ent.grid(row=i, column=0)
            load_info.append(str_no_ent)

        add_ent_btn = Button(master=frame, text="Add Manifest", command=lambda : self.update_added_manifests(load_info, man_date_ent.get(), man_no_ent.get()))
        add_ent_btn.grid(row=7, column=0, sticky="w")

        save_csv_btn = Button(master=frame, text='Save CSV', command=self.model.save_csv)
        save_csv_btn.grid(row=7, column=1)

        man_date_ent.focus()
    
    def added_manifests(self):
        frame = Frame(self.root)
        frame.grid(row=8, column=0)

        title_lbl = Label(master=frame, text='Added Manifests')
        title_lbl.grid(row=0, column=0)

        listbox = Listbox(frame, height=10, listvariable=self.man_var)

        scroll = Scrollbar(master=frame, orient=VERTICAL, command=listbox.yview)
        listbox.configure(yscrollcommand=scroll.set)

        listbox.grid(row=1, column=0, columnspan=3)
        scroll.grid(row=1, column=2)
    
    def update_added_manifests(self, load_info, date, num):
        self.model.add_manifest(load_info, date, num)
        manifests = self.model.get_added_manifests()
        show_manifests = [manifests[i][6] for i in range(1, len(manifests))]
        self.man_var.set(show_manifests)


