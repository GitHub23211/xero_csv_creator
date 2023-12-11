from tkinter import filedialog
from tkinter import *

import router
from pages import add_manifest
from pages import page_class

class Home(page_class.Page):
    def __init__(self, state):
        page_class.Page.__init__(self, state)
        self.invoice_info()
        self.save_dir()

    def invoice_info(self):
        frame = Frame(self)
        frame.grid(row=0, column=0, sticky="w")

        date_lbl = Label(master=frame, text="Invoice Date")
        num_lbl = Label(master=frame, text="Invoice Number")
        date_lbl.grid(row=0, column=0)
        num_lbl.grid(row=0, column=1)

        date_ent = Entry(master=frame)
        num_ent = Entry(master=frame)
        date_ent.grid(row=1, column=0)
        num_ent.grid(row=1, column=1)
    
    def save_dir(self):
        frame = Frame(self)
        frame.grid(row=1, column=0)

        get_dir = Button(master=frame, text="Choose save location", command=lambda : router.change_view(self, add_manifest.AddManifest, self.state))
        get_dir.grid()