from tkinter import Frame, Label, StringVar

class AddRigid(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
    
    def build(self):
        self.grid()
        self.show_item_line()
    
    def show_date(self):
        pass

    def show_item_line(self):
        for k, v in self.master.pricing.items():
            Label(self, text=self.generate_item_line(k, v)).grid()
    
    def generate_item_line(self, k, v):
        code = v[1]
        date = '11/2'
        if 'ST' in k:
            description = f'{date} (Sunday) - UNIT PRICE ${v[2]} + FL {self.master.fuel_levy * 100}%'
        else: 
            description = f'UNIT PRICE ${v[2]} + FL {self.master.fuel_levy * 100}%'
        return f'{code} {description}'