import csv
from dotenv import load_dotenv
from os import getenv
from json import load
from datetime import datetime, timedelta
from tkinter import messagebox
from operator import itemgetter
from tkinter import filedialog

class Model:
    def __init__(self):
        load_dotenv()
        self.inv_date = '1/1/99'
        self.inv_num = '0'
        self.manifests = [["*ContactName", "*InvoiceNumber", "Reference", "*InvoiceDate", "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "*AccountCode", "*TaxType"]]
        self.json_file = open('./store_pricing.json', mode='r')
        self.pricing = load(self.json_file)
    
    def set_inv_info(self, date, num):
        self.inv_date = date
        self.inv_num = num
    
    def save_csv(self):
        dir = filedialog.asksaveasfilename(initialdir='./', filetypes=[('CSV files', '*.csv')], defaultextension='.csv')
        csv_file = open(dir, mode='w', newline='')
        writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(self.manifests)
        csv_file.close()

    def generate_fixed_info(self):
        now = datetime.strptime(self.inv_date, '%d/%m/%y')
        week = now + timedelta(days=6)
        due = now + timedelta(days=30)
        reference = f"LOCAL: {now.strftime('%d/%m')}-{week.strftime('%d/%m/%y')}"
        return [
                getenv('CONTACT'), 
                self.inv_num.zfill(8),
                reference,
                now.strftime('%d/%m/%y'),
                due.strftime('%d/%m/%y'),
                1,
                getenv('CODE'),
                getenv('TAX')
            ]

    def add_manifest(self, m, man_date, man_num):
        store_nums = [x for x in filter(lambda x : x.get() != '', m)]
        try:
            loads = [self.pricing[x.get()] for x in store_nums]
            loads.sort(key=itemgetter(1), reverse=True)
            for i in range(0, len(loads)):
                #Generate fixed columns
                row_to_add = self.generate_fixed_info()

                #Inventory Code
                row_to_add.insert(5, self.choose_inv_code(i))

                #Description
                row_to_add.insert(6, f'{man_date} - {store_nums[i].get()} - {loads[i][0]} - {man_num}')

                #UnitAmount i.e. Price
                row_to_add.insert(8, self.choose_unit_amount(i, loads[i][1]))

                self.manifests.append(row_to_add)
        except Exception as e:
            messagebox.showerror('Error', f'Store number {e} does not exist')

    def choose_inv_code(self, i):
        if i == 0:
            return "AD-PRIM"
        return "DROP-RATE"

    def choose_unit_amount(self, i, price):
        if i == 0:
            return price
        return '50'

    def cleanup(self):
        self.json_file.close()