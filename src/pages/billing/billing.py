from tkinter import DoubleVar, StringVar, messagebox, filedialog
from datetime import datetime, timedelta
import openpyxl as excel
from re import compile
from os import listdir

from components.top import Top
from .b_ui import billingUI

class Billing(Top):
    def __init__(self, root, model, width, height, close_win_handler):
        Top.__init__(self, root, model, billingUI, width, height, close_win_handler)
        self.prices = self.model.billing
        self.date_var = StringVar(value='')
        self.prog_lbl_var = StringVar(value='Ready')
        self.prog_var = DoubleVar(value=0.0)
        self.max_prog_var = DoubleVar(value=0.0)
        self.curr_view.build()
    
    def increment_progress(self, val):
        self.prog_var.set(val)

    def submit(self, btn):
        try:
            self.prog_var.set(0.0)
            btn.config(state='disabled')
            self.model.save_csv(self.create_billing(self.date_var.get()))
            messagebox.showinfo('Success', 'Successfully created billing!')
            self.prog_lbl_var.set('Complete!')
            btn.config(state='normal')
        except Exception as e:
            messagebox.showerror('Error', e)
            btn.config(state='normal')
        finally:
            self.focus()

    def create_billing(self, date):
        try:
            bill_date = datetime.strptime(date, '%d/%m/%y')
            due_date = bill_date + timedelta(10)
            billing = [["*ContactName", "*InvoiceNumber", "*InvoiceDate", "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "*AccountCode", "*TaxType"]]
            data = self.extract_data()
            for emp in data:
                name = emp[0]
                bill_ref = emp[1]
                for key, value in emp[2].items():
                    item_code = self.prices[key][0]
                    description = self.prices[key][1]
                    price = self.prices[key][2]
                    num_loads = value
                    row_to_add = [name, bill_ref, bill_date.strftime('%d/%m/%y'), due_date.strftime('%d/%m/%y'), item_code, description, num_loads, price, '160', 'BAS Excluded']
                    billing.append(row_to_add)
            return billing
        except ValueError as e:
            raise Exception('Please enter a valid date')
        except Exception as e:
            raise e
        
    def get_load_amount(self, row):
        try:
            if 'OTHERS' in row:
                return (row[0], row[1])
            if 'LOCAL' in row:
                return (row[0], row[1])
            if 'DEE WHY' in row:
                return (row[0], row[1])
            if 'NTH.SYD' in row:
                return (row[0], row[1])
            if 'MDC-LOADS' in row:
                return (row[0], row[1])
            if 'TOTAL HOURS' in row:
                return (row[0], row[1])
            else:
                return (None, None)
        except Exception as e:
            print(f'{row} has error : {e}\n')

    def extract_data(self):
        messagebox.showinfo('Info', 'Select the folder that contains the employee tax invoices')
        rootdir = filedialog.askdirectory(initialdir='./')
        if rootdir == '':
            raise Exception('No directory chosen')
        
        regex = compile('.*xlsx$')
        spreadsheets = []
        files = listdir(rootdir)

        for file in files:
            if regex.match(file):
                spreadsheets.append(file)
        if len(spreadsheets) == 0:
            raise Exception('No Excel files found in that directory.')

        data = []
        self.prog_lbl_var.set('Creating billing...')

        for i, spreadsheet in enumerate(spreadsheets):
            wb = excel.load_workbook(f'{rootdir}/{spreadsheet}', data_only=True)
            sheets = wb.sheetnames
            latest = wb[sheets[len(sheets) - 1]]
            emp = [latest['A1'].value, latest['F4'].value, {}]
            
            for row in latest.values:
                load, amount = self.get_load_amount(row)
                if load is not None and amount is not None:
                    emp[2][load] = amount
            
            self.increment_progress(100*((i+1)/len(spreadsheets)))
            self.update()
            data.append(emp)

        return data