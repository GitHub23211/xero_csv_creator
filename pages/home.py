import tkinter as tk
from pages import add_manifest
from tkinter import filedialog

class Home():
    def __init__(self, root):
        self.root = root
        self.invoice_info()
        self.save_dir()

    def invoice_info(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, sticky="w")

        date_lbl = tk.Label(master=frame, text="Invoice Date")
        num_lbl = tk.Label(master=frame, text="Invoice Number")
        date_lbl.grid(row=0, column=0)
        num_lbl.grid(row=0, column=1)

        date_ent = tk.Entry(master=frame)
        num_ent = tk.Entry(master=frame)
        date_ent.grid(row=1, column=0)
        num_ent.grid(row=1, column=1)
    
    def save_dir(self):
        frame = tk.Frame(self.root)
        frame.grid(row=1, column=0)

        get_dir = tk.Button(master=frame, text="Choose save location", command=lambda : add_manifest.AddManifest(self.root))
        get_dir.grid()