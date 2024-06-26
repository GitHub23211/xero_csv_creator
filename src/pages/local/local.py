from .inv_info import InvoiceInfo
from .add_local import AddLocal
from components.top import Top
from components.invoice import Invoice
from components.validators.date_validator import DateValidator

class Local(Top):
    def __init__(self, root, model, width, height, close_win_handler):
        Top.__init__(self, root, model, InvoiceInfo, width, height, close_win_handler)
        self.invoice = Invoice(self.model.get_local_pricing(), self.model.get_invoice_info())
        self.curr_view.build()

    def navigate_add_manifests(self, date, num):
        if date == '' or num == '':
            raise Exception('Please enter an invoice date and number')
        if not DateValidator().validate(date):
            raise Exception('Date is invalid')
        
        self.invoice.set_date_num(date, num)
        self.switch_view(AddLocal)
        self.curr_view.build()
    
    def save_csv(self):
        self.model.save_csv(self.invoice.get_completed())
    
    def add_manifest(self, man_num, man_date, trailer_num, store_nums, loaded):
        stores = [x for x in filter(lambda x : x.get() != '', store_nums)]
        return self.invoice.append_manifest(man_num, man_date, trailer_num, stores, loaded)

    def delete_manifest(self, num_added):
        self.invoice.delete_manifest(num_added)
    
    def get_invoice(self):
        return self.invoice.get_invoice()
    
    def get_inv_date(self):
        return self.invoice.get_inv_date()

    def get_num_manifests(self):
        return self.invoice.get_num_manifests()