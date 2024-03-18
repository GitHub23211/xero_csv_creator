from tkinter import Frame, Label, Entry, Button, ttk

class billingUI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

    def build(self):
        self.grid(row=0, column=0, sticky=('n', 's', 'e', 'w'))
        self.master.columnconfigure(0, weight=1)
        self.columnconfigure([i for i in range(0, 6)], weight=1)
        self.grid()
        self.date()
        self.save_button()
        self.progress_bar()
    
    def date(self):
        f = Frame(self)
        f.grid(row=0, column=0, padx=10, pady=10)
        Label(f, text='Start Work Date (dd/mm/yy)').grid(row=0, column=0)
        Entry(f, textvariable=self.master.date_var).grid(row=0, column=1)

    def save_button(self):
        Button(self, text='Create CSV', command=self.master.submit).grid(row=1, column=0, pady=10)

    def progress_bar(self):
        Label(self, textvariable=self.master.prog_lbl_var).grid(row=2, column=0, pady=5)
        ttk.Progressbar(self, orient='horizontal', length=200, mode='determinate', variable=self.master.prog_var, value=self.master.prog_var.get()).grid(row=3, column=0)