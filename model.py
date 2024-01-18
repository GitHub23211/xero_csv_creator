from csv import writer, QUOTE_MINIMAL
from re import search
from copy import deepcopy
from dotenv import load_dotenv
from os import getenv
from json import load
from datetime import datetime, timedelta

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
        to_save = deepcopy(self.manifests)
        dir = filedialog.asksaveasfilename(initialdir='./', filetypes=[('CSV files', '*.csv')], defaultextension='.csv')
        csv_file = open(dir, mode='w', newline='')
        csv_writer = writer(csv_file, delimiter=",", quotechar='"', quoting=QUOTE_MINIMAL)
        self.add_reference(to_save)
        csv_writer.writerows(to_save)
        csv_file.close()
    
    def add_reference(self, list):
        last_man_date = search('[0-9]{1,2}/[0-9]{1,2}/[0-9]{2}', list[-1][5])
        for i in range(1, len(list)):
            list[i].insert(2, f"LOCAL: {self.inv_date}-{last_man_date.group(0)}")

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

    def add_manifest(self, m, man_date, man_num, index):
        store_nums = [x for x in filter(lambda x : x.get() != '', m)]
        try:
            loads = [self.pricing[x.get()] for x in store_nums]
            loads.sort(key=itemgetter(2), reverse=True)
            for i in range(0, len(loads)):
                #Generate fixed columns
                row_to_add = self.generate_fixed_info()

                #Inventory Code
                row_to_add.insert(4, 'AD-PRIM' if i == 0 and man_num else 'DROP-RATE')

                #Description
                row_to_add.insert(5, f'{man_date} - {loads[i][0]} - {loads[i][1]}{f" - {man_num}" if i == 0 and man_num else ""}')

                #UnitAmount i.e. Price
                row_to_add.insert(7, loads[i][2] if i == 0 and man_num else '50')

                self.manifests.append(row_to_add) if index == -1 else self.manifests.insert(index, row_to_add)
        except Exception as e:
            raise e

    def cleanup(self):
        self.json_file.close()