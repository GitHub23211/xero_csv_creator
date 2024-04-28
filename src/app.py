from tkinter import Tk, Button

from pages.rigid.rigid import Rigid
from pages.local.local import Local
from pages.billing.billing import Billing
from pages.stores.stores import Stores
import model

class App(Tk):
    def __init__(self, model):
        Tk.__init__(self)
        self.minsize(300, 180)
        self.title("Xero Invoice Creator")
        self.model = model
        self.create_menu()

    def create_menu(self):
        rigid_btn = Button(self, text='Rigid Invoicing', command=lambda: self.open_window(Rigid, rigid_btn, 600, 300))
        local_btn = Button(self, text='Local Invoicing', command=lambda : self.open_window(Local, local_btn, 270, 350))
        billing_btn = Button(self, text='Employee Pay', command=lambda: self.open_window(Billing, billing_btn, 320, 190))
        stores_btn = Button(self, text='Store Pricing', command=lambda: self.open_window(Stores, stores_btn, 400, 190))
        
        rigid_btn.place(relx=0.5, rely=0.2, anchor='center', relwidth=0.4)
        local_btn.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.4)
        billing_btn.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.4)
        stores_btn.place(relx=0.5, rely=0.8, anchor='center', relwidth=0.4)

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
