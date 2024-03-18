from tkinter import Frame, Label, Entry, Button, ttk

class billingUI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

    def build(self):
        self.master.columnconfigure(0, weight=1)
        self.columnconfigure([i for i in range(0, 6)], weight=1)
        self.grid()
        self.date()
        self.save_button()
        self.progress_bar()
    
    def date(self):
        Label(self, text='Start Work Date (dd/mm/yy)').grid(row=0, column=0, padx=5, pady=5)
        Entry(self, textvariable=self.master.date_var).grid(row=0, column=1, pady=5)

    def save_button(self):
        Button(self, text='Create CSV', command=self.master.submit).grid(row=3, column=0, columnspan=2, pady=8)

    def progress_bar(self):
        l = Label(self, textvariable=self.master.prog_lbl_var)
        p = ttk.Progressbar(self, orient='horizontal', length=200, mode='determinate', variable=self.master.prog_var, value=self.master.prog_var.get())
        
        l.grid(row=1, column=0, columnspan=2, sticky=('w', 'e'), pady=2.5)
        p.grid(row=2, column=0, columnspan=2, sticky=('w', 'e'), pady=2.5)