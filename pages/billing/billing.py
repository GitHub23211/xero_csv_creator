from tkinter import StringVar, messagebox, filedialog
from datetime import datetime, timedelta
import openpyxl as excel
from re import compile
from os import walk

from components import top
from pages.billing import b_ui

class Billing(top.Top):
    def __init__(self, root, model, width, height):
        top.Top.__init__(self, root, model, b_ui.billingUI, width, height)
        self.prices = self.model.billing
        self.date_var = StringVar(value='')
        self.curr_view.build()

    def submit(self):
        try:
            self.model.save_csv(self.create_billing(self.date_var.get()))
        except Exception as e:
            messagebox.showerror('Error', e)

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
        rootdir = filedialog.askdirectory(initialdir='./')
        print(rootdir)
        if rootdir == '':
            raise Exception('No directory chosen')
        
        regex = compile('.*xlsx$')
        spreadsheets = []
        data = []

        for root, dis, files in walk(rootdir):
            for file in files:
                if regex.match(file):
                    spreadsheets.append(file)

        for spreadsheet in spreadsheets:
            wb = excel.load_workbook(f'{rootdir}/{spreadsheet}', data_only=True)
            sheets = wb.sheetnames
            latest = wb[sheets[len(sheets) - 1]]
            emp = [latest['A1'].value, latest['F4'].value, {}]
            
            for row in latest.values:
                load, amount = self.get_load_amount(row)
                if load is not None and amount is not None:
                    emp[2][load] = amount
            
            data.append(emp)

        return data