from tkinter import Tk, Button

from pages.billing import billing
from pages.local import local
import model

class App(Tk):
    def __init__(self, model):
        Tk.__init__(self)
        self.maxsize(200, 130)
        self.title("Xero Invoice Creator")
        self.model = model
        self.protocol("WM_DELETE_WINDOW", self.model.cleanup)
        self.create_menu()

    def create_menu(self):
        l_tab = Button(self, text='Local Invoicing', command=lambda : self.open_window(local.Local, l_tab, 270, 350))
        b_tab = Button(self, text='Billing', command=lambda: self.open_window(billing.Billing, b_tab, 320, 190))

        l_tab.place(relx=0.5, rely=0.3, anchor='center', relwidth=0.5)
        b_tab.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.5)

    def open_window(self, window, btn, width, height):            
        btn.config(state='disabled')
        win = window(self, self.model, width, height, lambda: self.on_win_close(win, btn))
    
    def on_win_close(self, win, btn):
        btn.config(state='normal')
        win.destroy()

if __name__ == '__main__':
    model = model.Model()
    app = App(model)
    app.mainloop()
