from tkinter import StringVar, BooleanVar, messagebox
from operator import itemgetter
from datetime import datetime, timedelta
from copy import deepcopy
from re import search
from os import getenv
from dotenv import load_dotenv

from components import top
from pages.local import inv_info, add_local

MAN_NUM_LENGTH = 7

class Local(top.Top):
    def __init__(self, root, model, width, height, close_func):
        top.Top.__init__(self, root, model, inv_info.invoiceInfo, width, height, close_func)
        load_dotenv()
        self.invoice = [["*ContactName", "*InvoiceNumber", "Reference", "*InvoiceDate", "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "*AccountCode", "*TaxType"]]
        self.inv_date = '1/1/1990'
        self.inv_num = '-1'
        self.pricing = self.model.pricing
        self.man_var = StringVar(value=[])
        self.man_date_ent = None
        self.man_num_ent = None
        self.lbox = None
        self.load_info = []
        self.entered_man_nums = set()
        self.loaded_check = None
        self.loaded = BooleanVar(value=False)
        self.curr_view.build()

    def nav_add_manifests(self, date, num):
        if date == '' or num == '':
            messagebox.showerror('Error', 'Please enter an invoice date and number')
            return

        self.inv_date = date
        self.inv_num = num
        self.switch_view(add_local.AddLocal)
        self.curr_view.build()

    def save_csv(self):
        try:
            self.model.save_csv(self.add_reference())
        except Exception as e:
            messagebox.showerror('Error', e)
    
    def add_reference(self):
        complete = deepcopy(self.invoice)
        last_man_date = self.find_last_man(complete)
        for i in range(1, len(complete)):
            complete[i].insert(2, f"LOCAL: {self.inv_date}-{last_man_date.group(0)}")
        return complete

    def find_last_man(self, invoice): 
        regex = '[0-9]{1,2}/[0-9]{1,2}/[0-9]{2}'
        result = None
        i = -1
        while not result:
            result = search(regex, invoice[i][5])
            i = i - 1
        if result is None:
            raise Exception('Could not get the last manifest date')
        return result
        
    def add_manifest(self, event=None):
        try:
            self.update_added_manifests()
            self.clear_entries()
        except Exception as e:
            messagebox.showerror('Error', e)
        finally:
            self.focus()
            self.man_num_ent.focus()
    
    def clear_entries(self):
        for i in range(0, 3):
            self.load_info[i].delete(0, 'end')

        self.man_num_ent.delete(0, 'end')
        self.lbox.select_clear('active', 'end')
        self.lbox.yview_moveto(1)

        if self.loaded.get():
            self.loaded_check.invoke()
            
    def update_added_manifests(self):
        try:
            self.append_to_invoice()
            manifests = self.invoice
            show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
            self.man_var.set(show_manifests)
        except Exception as e:
           raise e
        
    def append_to_invoice(self):
        store_nums = [x for x in filter(lambda x : x.get() != '', self.load_info)]
        man_num = self.man_num_ent.get()

        if len(man_num) != MAN_NUM_LENGTH:
            raise Exception('Invalid manifest number')
        if man_num in self.entered_man_nums:
            raise Exception('Manifest number has already been entered')
        if len(store_nums) <= 0:
            raise Exception('No store numbers entered')

        try:
            loads = [self.pricing[x.get()] for x in store_nums]
        except Exception as e:
            raise Exception(f'Store number {e} does not exist')

        loads.sort(key=itemgetter(2), reverse=True)
        for i in range(0, len(loads)):
            self.invoice.append(self.append_manifest(man_num, loads, i))

        if self.loaded.get():
            self.invoice.append(self.append_allowance())
    
    def append_allowance(self):
        allowance = self.generate_fixed_info()
        allowance.insert(4, self.pricing['ALLWNCE'][0])
        allowance.insert(5, self.pricing['ALLWNCE'][1])
        allowance.insert(7, self.pricing['ALLWNCE'][2])
        return allowance

    def generate_fixed_info(self):
        now = datetime.strptime(self.inv_date, '%d/%m/%y')
        due = now + timedelta(days=30)
        return [
                getenv('CONTACT'), 
                self.inv_num.zfill(8),
                now.strftime('%d/%m/%y'),
                due.strftime('%d/%m/%y'),
                1,
                getenv('CODE'),
                getenv('TAX')
            ]

    def append_manifest(self, man_num, loads, i):
        #Generate fixed columns
        row_to_add = self.generate_fixed_info()

        #Inventory Code
        row_to_add.insert(4, 'AD-PRIM' if i == 0 and man_num else 'DROP-RATE')

        #Description
        self.entered_man_nums.add(man_num)
        row_to_add.insert(5, f'{self.man_date_ent.get()} - {loads[i][0]} - {loads[i][1]}{f" - {man_num}" if i == 0 and man_num else ""}')

        #UnitAmount i.e. Price
        row_to_add.insert(7, loads[i][2] if i == 0 and man_num else '50')

        return row_to_add

    def delete_manifest(self):
        manifests = self.invoice
        if len(manifests) > 1:
            deleted_man_num = manifests.pop()[5][-MAN_NUM_LENGTH:]
            self.entered_man_nums.discard(deleted_man_num)
            show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
            self.man_var.set(show_manifests)