from pages import page

class Local(page.Page):
    def __init__(self, root, model, home):
        page.Page.__init__(self, root, model)
        self.curr_frame = None
        self.grid()
        self.build(home(self, self.model))

    def build(self, new_page):
        if self.curr_frame is not None:
            self.curr_frame.destroy()
        self.curr_frame = new_page
        self.curr_frame.build()
