from tkinter import *

from pages import page_class

class AddManifest(page_class.Page):
    def __init__(self, state):
        page_class.Page.__init__(self, state, 300, 700)
        self.manifest_info()

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

        add_ent_btn = Button(master=frame, text="Add Manifest", command=lambda : self.model.add_manifest(load_info, man_date_ent.get(), man_no_ent.get()))
        add_ent_btn.grid(row=7, column=0, sticky="w")

        save_csv_btn = Button(master=frame, text='Save CSV', command=self.model.save_csv)
        save_csv_btn.grid(row=7, column=1)