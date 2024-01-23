from tkinter import Toplevel

class Top(Toplevel):
    def __init__(self, root, model, page, title, width, height):
        Toplevel.__init__(self, root)
        self.model = model
        self.title = title
        self.minsize(width, height)
        self.curr_view = None
        self.switch_view(page)
    
    def switch_view(self, new_page):
        if self.curr_view is not None:
            self.curr_view.destroy()
        self.curr_view = new_page(self, self.model)
        self.curr_view.build()
        
