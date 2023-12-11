from tkinter import *

import router
from pages import add_manifest
from pages import page_class

class Home(page_class.Page):
    def __init__(self, state):
        page_class.Page.__init__(self, state, 200, 200)
        self.invoice_info()

    def invoice_info(self):
        frame = Frame(self)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        date_lbl = Label(master=frame, text="Invoice Date")
        num_lbl = Label(master=frame, text="Invoice Number")
        date_lbl.grid(row=0, column=0, sticky="w")
        num_lbl.grid(row=1, column=0, sticky="w")

        date_ent = Entry(master=frame)
        num_ent = Entry(master=frame)
        date_ent.grid(row=0, column=1)
        num_ent.grid(row=1, column=1)

        man_page_btn = Button(master=frame, text='Start Adding Manifests', command=lambda : self.nav_add_manifests(date_ent.get(), num_ent.get()))
        man_page_btn.grid(row=3, column=0)
    
    def nav_add_manifests(self, date, num):
        self.model.set_inv_info(date, num)
        router.change_view(self, add_manifest.AddManifest, self.state)