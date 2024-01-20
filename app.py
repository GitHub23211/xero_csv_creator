import tkinter as tk
from atexit import register

from pages import home
import model

class App(tk.Tk):
    def __init__(self, model, page):
        tk.Tk.__init__(self)
        self.curr_frame = None
        self.model = model
        self.switch_frames(page)
    
    def switch_frames(self, new):
        new_frame = new(self, self.model)
        if self.curr_frame is not None:
            self.curr_frame.destroy()
        self.curr_frame = new_frame
        self.curr_frame.grid()

if __name__ == '__main__':
    model = model.Model()
    app = App(model, home.Home)
    register(model.cleanup)
    app.mainloop()
