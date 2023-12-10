from datetime import datetime, timedelta, date
from dotenv import load_dotenv
from os import getenv
from tkinter import messagebox
import atexit
import csv
import json
from operator import itemgetter

def setup_csv():
    headings = ["*ContactName", "*InvoiceNumber", "Reference", "*InvoiceDate", "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "*AccountCode", "*TaxType"]
    writer.writerow(headings)

def generate_fixed_info(inv_num, inv_date):
       now = datetime.strptime(inv_date, '%d/%m/%y')
       week = now + timedelta(days=6)
       due = now + timedelta(days=30)
       reference = f"LOCAL: {now.strftime('%d/%m')}-{week.strftime('%d/%m/%y')}"
       return [
        getenv('CONTACT'), 
        inv_num.zfill(8),
        reference,
        now.strftime('%d/%m/%y'),
        due.strftime('%d/%m/%y'),
        1,
        getenv('CODE'),
        getenv('TAX')
    ]

def add_manifest(m, inv_num, inv_date, man_date, man_num):
    store_nums = [x for x in filter(lambda x : x.get() != '', m)]
    try:
        loads = [pricing[x.get()] for x in store_nums]
        loads.sort(key=itemgetter(1), reverse=True)
        for i in range(0, len(loads)):
            #Generate fixed columns
            row_to_add = generate_fixed_info(inv_num, inv_date)

            #Inventory Code
            row_to_add.insert(5, choose_inv_code(i))

            #Description
            row_to_add.insert(6, f'{man_date} - {store_nums[i].get()} - {loads[i][0]} - {man_num}')

            #UnitAmount i.e. Price
            row_to_add.insert(8, choose_unit_amount(i, loads[i][1]))

            writer.writerow(row_to_add)
    except Exception as e:
        messagebox.showerror('Error', f'Store number {e} does not exist')

def choose_inv_code(i):
    if i == 0:
          return "AD-PRIM"
    return "DROP-RATE"

def choose_unit_amount(i, price):
     if i == 0:
          return price
     return '50'

def cleanup():
    print("Closing json and csv files")
    raw_json.close()
    new_csv.close()

load_dotenv()
raw_json = open('store_pricing.json', mode='r')
new_csv = open("sample.csv", mode="w", newline='')
pricing = json.load(raw_json)
writer = csv.writer(new_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
setup_csv()

atexit.register(cleanup)