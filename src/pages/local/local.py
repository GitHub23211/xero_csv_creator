from tkinter import StringVar, BooleanVar, messagebox
from components import top, invoice
from pages.local import inv_info, add_local

class Local(top.Top):
    def __init__(self, root, model, width, height, close_func):
        top.Top.__init__(self, root, model, inv_info.invoiceInfo, width, height, close_func)
        self.invoice = invoice.Invoice(self.model.pricing)
        self.man_date_ent = None
        self.man_num_ent = None
        self.loaded_checkbox_widget = None
        self.lbox = None
        self.stores_nums = []
        self.man_var = StringVar(value=[])
        self.loaded = BooleanVar(value=False)
        self.curr_view.build()

    def navigate_add_manifests(self, date, num):
        if date == '' or num == '':
            messagebox.showerror('Error', 'Please enter an invoice date and number')
            return
        
        self.invoice.set_date_num(date, num)
        self.switch_view(add_local.AddLocal)
        self.curr_view.build()
    
    def save_csv(self):
        try:
            self.model.save_csv(self.invoice.get_completed())
        except Exception as e:
            messagebox.showerror('Error', e)
    
    def add_manifest(self, event=None):
        try:
            self.update_invoice()
            self.clear_widgets()
        except Exception as e:
            messagebox.showerror('Error', e)
        finally:
            self.focus()
            self.man_num_ent.focus()
        
    def update_invoice(self, event=None):
        stores = [x for x in filter(lambda x : x.get() != '', self.stores_nums)]
        man_num = self.man_num_ent.get()
        man_date = self.man_date_ent.get()

        try:
            self.invoice.append_manifest(man_num, man_date, stores, self.loaded.get())
            self.update_lbox_contents(self.invoice.get_invoice())
        except Exception as e:
            raise e

    def clear_widgets(self):
        for i in range(0, 3):
            self.stores_nums[i].delete(0, 'end')

        self.man_num_ent.delete(0, 'end')
        self.lbox.yview_moveto(1)

        if self.loaded.get():
            self.loaded_checkbox_widget.invoke()
        
    def delete_manifest(self):
        self.invoice.delete_manifest()
        self.update_lbox_contents(self.invoice.get_invoice())
    
    def update_lbox_contents(self, invoice):
        show_manifests = [f'{invoice[i][5]} - ${invoice[i][7]}' for i in range(1, len(invoice))]
        self.man_var.set(show_manifests)
    
    def get_inv_date(self):
        return self.invoice.get_inv_date()