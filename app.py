from tkinter import Tk, Button

from pages.billing import billing
from pages.local import local
import model

class App(Tk):
    def __init__(self, model):
        Tk.__init__(self)
        self.minsize(270, 350)
        self.title("Xero Invoice Creator")
        self.model = model
        self.create_menu()

    def create_menu(self):
        l_tab = Button(self, text='Local Invoicing', command=lambda : self.open_window(local.Local, l_tab, 270, 350))
        b_tab = Button(self, text='Billing', command=lambda : self.open_window(billing.Billing, b_tab, 350, 250))

        l_tab.grid()
        b_tab.grid()
    
    def open_window(self, window, btn, width, height):
        def on_win_close(win, btn):
            btn.config(state='normal')
            win.destroy()
            
        btn.config(state='disabled')
        win = window(self, self.model, width, height, lambda: on_win_close(win, btn))

if __name__ == '__main__':
    model = model.Model()
    app = App(model)
    app.mainloop()
