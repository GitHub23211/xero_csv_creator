from .inv_info import InvoiceInfo
from .add_local import AddLocal
from components.top import Top
from components.invoice import Invoice

class Local(Top):
    def __init__(self, root, model, width, height, close_win_handler):
        Top.__init__(self, root, model, InvoiceInfo, width, height, close_win_handler)
        self.invoice = Invoice(self.model.pricing)
        self.curr_view.build()

    def navigate_add_manifests(self, date, num):
        if date == '' or num == '':
            raise Exception('Please enter an invoice date and number')
        
        self.invoice.set_date_num(date, num)
        self.switch_view(AddLocal)
        self.curr_view.build()
    
    def save_csv(self):
        self.model.save_csv(self.invoice.get_completed())
    
    def add_manifest(self, man_num, man_date, store_nums, loaded):
        stores = [x for x in filter(lambda x : x.get() != '', store_nums)]
        return self.invoice.append_manifest(man_num, man_date, stores, loaded)

    def delete_manifest(self):
        self.invoice.delete_manifest()
    
    def get_invoice(self):
        return self.invoice.get_invoice()
    
    def get_inv_date(self):
        return self.invoice.get_inv_date()