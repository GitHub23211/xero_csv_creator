from tkinter import Tk, Button
from atexit import register

from pages import top, billing
from pages.local import home
import model

#CONSTANTS
MAX_WIND_COUNT = 4

class App(Tk):
    def __init__(self, model):
        Tk.__init__(self)
        self.minsize(270, 350)
        self.title("Xero Invoice Creator")
        self.model = model
        self.wind_count = 0
        self.max_wind = MAX_WIND_COUNT
        self.create_menu()
    
    def create_menu(self):
        # r_tab = home.Home(self.notebook, self.model)
        # f_tab = home.Home(self.notebook, self.model)
        l_tab = Button(self, text='Local Invoicing', command=lambda : self.open_window(home.Home, 'Local Invoice', 270, 350))
        b_tab = Button(self, text='Billing', command=lambda : self.open_window(billing.Billing))

        l_tab.grid()
        b_tab.grid()
    
    def open_window(self, page, title='New Window', width=300, height=300):
        if self.wind_count < self.max_wind:
            top.Top(self, self.model, page, title, width, height)
            self.wind_count = self.wind_count + 1

if __name__ == '__main__':
    model = model.Model()
    app = App(model)
    register(model.cleanup)
    app.mainloop()
