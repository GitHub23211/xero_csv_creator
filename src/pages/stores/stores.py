from components.top import Top
from .ui import UI

class Stores(Top):
    def __init__(self, root, model, width, height, close_win_handler):
        Top.__init__(self, root, model, UI, width, height, close_win_handler)
        self.prices = self.model.pricing
        self.columnconfigure(0, weight=1)
        self.curr_view.build()