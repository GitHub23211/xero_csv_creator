import csv
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
        writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self.add_reference(to_save)
        writer.writerows(to_save)
        csv_file.close()
    
    def add_reference(self, list):
        first_man_date = list[1][2]
        last_man_date = list[len(list) - 1][2]
        for i in range(1, len(list)):
            list[i].insert(2, f"LOCAL: {first_man_date}-{last_man_date}")

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

    def add_manifest(self, m, man_date, man_num):
        store_nums = [x for x in filter(lambda x : x.get() != '', m)]
        try:
            loads = [self.pricing[x.get()] for x in store_nums]
            loads.sort(key=itemgetter(2), reverse=True)
            for i in range(0, len(loads)):
                #Generate fixed columns
                row_to_add = self.generate_fixed_info()

                #Inventory Code
                row_to_add.insert(4, self.choose_inv_code(i))

                #Description
                if i == 0:
                    row_to_add.insert(5, f'{man_date} - {loads[i][0]} - {loads[i][1]} - {man_num}')
                else:
                    row_to_add.insert(5, f'{man_date} - {loads[i][0]} - {loads[i][1]}')

                #UnitAmount i.e. Price
                row_to_add.insert(7, self.choose_unit_amount(i, loads[i][2]))

                self.manifests.append(row_to_add)
        except Exception as e:
            raise e


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