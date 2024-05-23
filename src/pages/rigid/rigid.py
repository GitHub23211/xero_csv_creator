from components.top import Top
from .add_rigid import AddRigid
from components.rigid_invoice import RigidInvoice

class Rigid(Top):
    def __init__(self, root, model, width, height, close_win_handler):
        Top.__init__(self, root, model, AddRigid, width, height, close_win_handler)
        self.pricing = self.model.get_rigid_pricing().items()
        self.fuel_levy = self.model.get_fuel_levy()
        self.invoice = RigidInvoice(self.model.get_invoice_info())
        self.columnconfigure(0, weight=1)
        self.curr_view.build()
    
    def save_csv(self, invoice):
        self.model.save_csv(invoice)