from tkinter import Toplevel

class Top(Toplevel):
    def __init__(self, root, model, frame, width, height, close_func):
        Toplevel.__init__(self, root)
        self.curr_view = None
        self.model = model
        self.minsize(width, height)
        self.protocol("WM_DELETE_WINDOW", close_func)
        self.switch_view(frame)
    
    def switch_view(self, new_frame):
        if self.curr_view is not None:
            self.curr_view.destroy()
        self.curr_view = new_frame(self)