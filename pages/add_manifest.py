from tkinter import *

from pages import page_class

class AddManifest(page_class.Page):
    def __init__(self, state):
        page_class.Page.__init__(self, state, 270, 350)
        self.man_var = StringVar(value=[])
        self.man_date_ent = None
        self.man_num_ent = None
        self.load_info = []
        self.manifest_input()
        self.store_input()
        self.added_manifests()

    def manifest_input(self):
        frame = Frame(self)
        frame.grid(row=0, column=0)

        man_date_lbl = Label(master=frame, text='Manifest Date')
        man_date_lbl.grid(row=0, column=0)

        man_num_lbl = Label(master=frame, text='Manifest Number')
        man_num_lbl.grid(row=0, column=1)

        self.man_date_ent = Entry(master=frame)
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
            add_ent_btn = Button(frame, text="Add Manifest", command=lambda : self.update_added_manifests(self.man_date_ent.get(), self.man_num_ent.get()))
            add_ent_btn.grid(row=1, column=1, padx=20, sticky=(E, W))

            del_ent_btn = Button(frame, text="Delete Last Entry", command=lambda : print("hi"))
            del_ent_btn.grid(row=2, column=1, padx=20, sticky=(E, W))

            save_csv_btn = Button(frame, text='Save CSV', command=self.model.save_csv)
            save_csv_btn.grid(row=3, column=1, padx=20, sticky=(E, W))
        buttons()   

    def added_manifests(self):
        frame = Frame(self)
        frame.grid(row=2, column=0, pady=10)

        title_lbl = Label(frame, text='Added Manifests')
        title_lbl.grid(row=0, column=0)

        listbox = Listbox(frame, width=50, listvariable=self.man_var)

        scroll = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
        listbox.configure(yscrollcommand=scroll.set)

        listbox.grid(row=1, column=0, sticky=E)
        scroll.grid(row=1, column=1, sticky=(N,S))

    def update_added_manifests(self, date, num):
        self.model.add_manifest(self.load_info, date, num)
        manifests = self.model.get_added_manifests()
        show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
        self.man_var.set(show_manifests)

    def delete_manifest(self):
        manifests = self.model.get_added_manifests()
        if len(manifests) > 1:
            manifests.pop()
            show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
            self.man_var.set(show_manifests)

