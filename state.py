class State():
    def __init__(self, root, model):
        self.root = root
        self.model = model

    def get_model(self):
        return self.model
    
    def get_root(self):
        return self.root