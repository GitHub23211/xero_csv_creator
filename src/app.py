from tkinter import Tk, Button

from pages.billing import Billing
from pages.local import Local
from pages.stores import Stores
import model

class App(Tk):
    def __init__(self, model):
        Tk.__init__(self)
        self.maxsize(200, 130)
        self.title("Xero Invoice Creator")
        self.model = model
        self.protocol("WM_DELETE_WINDOW", self.cleanup)
        self.create_menu()

    def create_menu(self):
        local_btn = Button(self, text='Local Invoicing', command=lambda : self.open_window(Local, local_btn, 270, 350))
        billing_btn = Button(self, text='Billing', command=lambda: self.open_window(Billing, billing_btn, 320, 190))
        stores_btn = Button(self, text='Store Pricing', command=lambda: self.open_window(Stores, stores_btn, 320, 190))

        local_btn.place(relx=0.5, rely=0.3, anchor='center', relwidth=0.5)
        billing_btn.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.5)

    def open_window(self, window, btn, width, height):            
        btn.config(state='disabled')
        win = window(self, self.model, width, height, lambda: self.on_win_close(win, btn))
    
    def on_win_close(self, win, btn):
        btn.config(state='normal')
        win.destroy()
    
    def cleanup(self):
        self.model.cleanup()
        self.destroy()

if __name__ == '__main__':
    model = model.Model()
    app = App(model)
    app.mainloop()
