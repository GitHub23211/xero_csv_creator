from tkinter import StringVar, BooleanVar, messagebox
from operator import itemgetter
from datetime import datetime, timedelta
from copy import deepcopy
from re import search
from os import getenv
from dotenv import load_dotenv

from components import top
from pages.local import inv_info, add_local

class Local(top.Top):
    def __init__(self, root, model, width, height):
        top.Top.__init__(self, root, model, inv_info.invoiceInfo, width, height)
        load_dotenv()
        self.invoice = [["*ContactName", "*InvoiceNumber", "Reference", "*InvoiceDate", "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "*AccountCode", "*TaxType"]]
        self.pricing = self.model.pricing
        self.inv_date = '1/1/1990'
        self.inv_num = '-1'
        self.man_var = StringVar(value=[])
        self.man_date_ent = None
        self.man_num_ent = None
        self.lbox = None
        self.lbox_index = -1
        self.load_info = []
        self.loaded_check = None
        self.loaded = BooleanVar(value=False)
        self.curr_view.build()

    def nav_add_manifests(self, date, num):
        if(date != '' and num != ''):
            self.inv_date = date
            self.inv_num = num
            self.switch_view(add_local.AddLocal)
            self.curr_view.build()
        else:
            messagebox.showerror('Error', 'Please enter an invoie date and number')

    def save_csv(self):
        self.model.save_csv(self.add_reference())
    
    def add_reference(self):
        complete = deepcopy(self.invoice)
        last_man_date = search('[0-9]{1,2}/[0-9]{1,2}/[0-9]{2}', complete[-1][5])
        for i in range(1, len(complete)):
            complete[i].insert(2, f"LOCAL: {self.inv_date}-{last_man_date.group(0)}")
        return complete

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

    def add_manifest(self):
        store_nums = [x for x in filter(lambda x : x.get() != '', self.load_info)]
        man_num = self.man_num_ent.get()
        index = self.lbox_index
        if len(store_nums) > 0:
            try:
                loads = [self.pricing[x.get()] for x in store_nums]
                loads.sort(key=itemgetter(2), reverse=True)
                for i in range(0, len(loads)):
                    #Generate fixed columns
                    row_to_add = self.generate_fixed_info()

                    #Inventory Code
                    row_to_add.insert(4, 'AD-PRIM' if i == 0 and man_num else 'DROP-RATE')

                    #Description
                    row_to_add.insert(5, f'{self.man_date_ent.get()} - {loads[i][0]} - {loads[i][1]}{f" - {man_num}" if i == 0 and man_num else ""}')

                    #UnitAmount i.e. Price
                    row_to_add.insert(7, loads[i][2] if i == 0 and man_num else '50')

                    self.invoice.append(row_to_add) if index == -1 else self.invoice.insert(index, row_to_add)
                if self.loaded.get():
                    allowance = self.generate_fixed_info()
                    allowance.insert(4, self.pricing['ALLWNCE'][0])
                    allowance.insert(5, self.pricing['ALLWNCE'][1])
                    allowance.insert(7, self.pricing['ALLWNCE'][2])
                    self.invoice.append(allowance) if index == -1 else self.invoice.insert(index+1, allowance)
            except Exception as e:
                raise e
            
    def append_manifest(self, event=None):
        try:
            self.update_added_manifests()
            for i in range(0, 3):
                self.load_info[i].delete(0, 'end')
            self.man_num_ent.delete(0, 'end')
            self.lbox.select_clear('active', 'end')
            self.lbox_index = -1
            self.lbox.yview_moveto(1)
            if self.loaded.get():
                self.loaded_check.invoke()
            self.man_num_ent.focus()
        except Exception as e:
            messagebox.showerror('Error', f'Store number {e} does not exist')
        
    def update_added_manifests(self):
        self.add_manifest()
        manifests = self.invoice
        show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
        self.man_var.set(show_manifests)

    def delete_manifest(self):
        manifests = self.invoice
        if len(manifests) > 1:
            manifests.pop()
            show_manifests = [f'{manifests[i][5]} - ${manifests[i][7]}' for i in range(1, len(manifests))]
            self.man_var.set(show_manifests)

    def update_lbox_index(self, event=None):
        if self.lbox.curselection()[0] == self.lbox_index - 2:
            self.lbox.select_clear('active', 'end')
            self.lbox_index = -1
        else:
            self.lbox_index = -1 if len(self.lbox.curselection()) == 0 else self.lbox.curselection()[0] + 2