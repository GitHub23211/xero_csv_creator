from tkinter import *

from pages import page_class

class AddManifest(page_class.Page):
    def __init__(self, state):
        page_class.Page.__init__(self, state)
        self.manifest_info()
        self.load_input()

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
    
    def load_input(self):
        frame = Frame(self.root)
        frame.grid(row=1, column=0, sticky="w")

        str_no_lbl = Label(master=frame, text="Store Number")
        str_no_lbl.grid(row=0, column=0)

        load_info = []
        for i in range(1, 4):
            str_no_ent = Entry(master=frame)
            str_no_ent.grid(row=i, column=0)
            load_info.append(str_no_ent)

        add_ent = Button(master=frame, text="Add Manifest", command=lambda : print("hey"))#main.add_manifest(load_info, num_ent.get(), mandate_ent.get(), date_ent.get(), manno_ent.get()))
        add_ent.grid(row=4, column=0, sticky="w")