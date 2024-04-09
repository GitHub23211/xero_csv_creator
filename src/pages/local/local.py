from tkinter import StringVar, BooleanVar, messagebox
from inv_info import InvoiceInfo
from add_local import AddLocal
from components.top import Top
from components.invoice import Invoice

class Local(Top):
    def __init__(self, root, model, width, height, close_func):
        Top.__init__(self, root, model, InvoiceInfo, width, height, close_func)
        self.invoice = Invoice(self.model.pricing)
        self.man_date_var = StringVar(value='')
        self.man_num_var = StringVar(value='')
        self.man_list = StringVar(value=[])
        self.loaded = BooleanVar(value=False)
        self.stores_nums = []
        self.curr_view.build()

    def navigate_add_manifests(self, date, num):
        if date == '' or num == '':
            messagebox.showerror('Error', 'Please enter an invoice date and number')
            return
        
        self.invoice.set_date_num(date, num)
        self.man_date_var.set(self.invoice.get_inv_date())
        self.switch_view(AddLocal)
        self.curr_view.build()
    
    def save_csv(self):
        try:
            self.model.save_csv(self.invoice.get_completed())
        except Exception as e:
            messagebox.showerror('Error', e)
    
    def add_manifest(self):
        try:
            self.update_invoice()
            self.reset_widgets()
        except Exception as e:
            messagebox.showerror('Error', e)
        
    def update_invoice(self):
        stores = [x for x in filter(lambda x : x.get() != '', self.stores_nums)]
        man_num = self.man_num_var.get()
        man_date = self.man_date_var.get()

        try:
            self.invoice.append_manifest(man_num, man_date, stores, self.loaded.get())
            self.update_lbox_contents(self.invoice.get_invoice())
        except Exception as e:
            raise e

    def reset_widgets(self):
        for i in range(0, 3):
            self.stores_nums[i].delete(0, 'end')
        self.man_num_var.set('')
        self.loaded.set(False)

    def delete_manifest(self):
        self.invoice.delete_manifest()
        self.update_lbox_contents(self.invoice.get_invoice())
    
    def update_lbox_contents(self, invoice):
        show_manifests = [f'{invoice[i][5]} - ${invoice[i][7]}' for i in range(1, len(invoice))]
        self.man_list.set(show_manifests)