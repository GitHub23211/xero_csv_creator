from tkinter import Frame, Label, Entry, Button, StringVar, messagebox
from components.validators.input_checker import InputChecker
class InvoiceInfo(Frame):
    def __init__(self, root):
         Frame.__init__(self, root)
         self.date_str = StringVar(value='')
         self.man_num = StringVar(value='')

    def build(self):
        self.grid()
        self.invoice_info()

    def invoice_info(self):
        f = Frame(self)
        date_lbl = Label(f, text="Invoice Date (dd/mm/yy)")
        num_lbl = Label(f, text="Invoice Number")
        date_ent = Entry(f, textvariable=self.date_str, validate='key', validatecommand=InputChecker(self, '[0-9/]*').create_tcl_wrapper())
        num_ent = Entry(f, textvariable=self.man_num, validate='key', validatecommand=InputChecker(self, '[0-9]*').create_tcl_wrapper())
        man_page_btn = Button(f, text='Start Adding Manifests', command=self.submit_date_num)

        f.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        date_lbl.grid(row=0, column=0, sticky="w")
        date_ent.grid(row=0, column=1)
        num_lbl.grid(row=2, column=0, sticky="w")
        num_ent.grid(row=2, column=1)
        man_page_btn.grid(row=3, column=0)

        date_ent.focus()
    
    def submit_date_num(self):
        try:
            self.master.navigate_add_manifests(self.date_str.get(), self.man_num.get())
        except Exception as e:
            messagebox.showerror('Error', e)
            self.focus()
