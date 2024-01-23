from tkinter import Tk
from tkinter.ttk import Notebook
from atexit import register

from pages import home, local
import model

class App(Tk):
    def __init__(self, model):
        Tk.__init__(self)
        self.minsize(270, 350)
        self.title("Xero Invoice Creator")
        self.model = model
        self.notebook = Notebook(self)
        self.create_tabs()
        self.notebook.grid()
    
    def create_tabs(self):
        # r_tab = home.Home(self.notebook, self.model)
        # f_tab = home.Home(self.notebook, self.model)
        l_tab = local.Local(self.notebook, self.model, home.Home)
        # b_tab =  home.Home(self.notebook, self.model)
        # self.notebook.add(r_tab, text='Rigid')
        # self.notebook.add(f_tab, text='Freezer')
        self.notebook.add(l_tab, text='Local')
        # self.notebook.add(b_tab, text='Billing')

if __name__ == '__main__':
    model = model.Model()
    app = App(model)
    register(model.cleanup)
    app.mainloop()
