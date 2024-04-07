from tkinter import Frame, Label, Entry, ttk, StringVar
from re import match, fullmatch

class invoiceInfo(Frame):
    def __init__(self, root):
         Frame.__init__(self, root)

    def build(self):
        self.grid()
        self.invoice_info()

    def invoice_info(self):
        frame = Frame(self)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        date_lbl = Label(frame, text="Invoice Date (dd/mm/yy)")
        num_lbl = Label(frame, text="Invoice Number")
        date_lbl.grid(row=0, column=0, sticky="w")
        num_lbl.grid(row=2, column=0, sticky="w")
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

        validate_date_wrapper = (self.register(validate_date), '%P', '%V')
        date_ent = Entry(frame, validate='all', validatecommand=validate_date_wrapper)
        num_ent = Entry(frame)
        date_ent.grid(row=0, column=1)
        num_ent.grid(row=2, column=1)

        man_page_btn = ttk.Button(frame, text='Start Adding Manifests', command=lambda : self.master.navigate_add_manifests(date_ent.get(), num_ent.get()))
        man_page_btn.grid(row=3, column=0)
        man_page_btn.state(['disabled'])

        date_err_lbl = Label(frame, textvariable=err, fg='red')
        date_err_lbl.grid(row=4, column=1)

        date_ent.focus()