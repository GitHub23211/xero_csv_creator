from tkinter import Frame, Label, Entry, StringVar, ttk, messagebox
from re import match, fullmatch

from pages import page
from pages.local import add_local

class Home(page.Page):
    def __init__(self, root, model):
        page.Page.__init__(self, root, model)

    def build(self):
        self.grid()
        self.invoice_info()

    def invoice_info(self):
        frame = Frame(self)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        err = StringVar(value='')

        def validate_date(s, op):
            err.set('')
            date_err_lbl.grid(row=4, column=1)
            valid = match('[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2}', s) is not None
            man_page_btn.state(['!disabled'] if valid else ['disabled'])
            if op == 'key':
                curr_valid = fullmatch('[0-9/]*', s) is not None
                if not curr_valid:
                    err.set('Numbers and / only')
                    date_err_lbl.grid(row=1, column=1)
                if len(s) > 8:
                    return False
                return curr_valid
            elif op == 'focusout':
                if not valid and len(s) > 0:
                    err.set('Invalid format')
                    date_err_lbl.grid(row=1, column=1)
            return valid

        date_lbl = Label(frame, text="Invoice Date (dd/mm/yy)")
        num_lbl = Label(frame, text="Invoice Number")
        date_lbl.grid(row=0, column=0, sticky="w")
        num_lbl.grid(row=2, column=0, sticky="w")

        validate_date_wrapper = (self.register(validate_date), '%P', '%V')
        date_ent = Entry(frame, validate='all', validatecommand=validate_date_wrapper)
        num_ent = Entry(frame)
        date_ent.grid(row=0, column=1)
        num_ent.grid(row=2, column=1)

        man_page_btn = ttk.Button(frame, text='Start Adding Manifests', command=lambda : self.nav_add_manifests(date_ent.get(), num_ent.get()))
        man_page_btn.grid(row=3, column=0)
        man_page_btn.state(['disabled'])

        date_err_lbl = Label(frame, textvariable=err, fg='red')
        date_err_lbl.grid(row=4, column=1)

        date_ent.focus()

    def nav_add_manifests(self, date, num):
        if(date != '' and num != ''):
            self.model.set_inv_info(date, num)
            self.master.switch_view(add_local.AddLocal)
        else:
            messagebox.showerror('Error', 'Please enter an invoie date and number')