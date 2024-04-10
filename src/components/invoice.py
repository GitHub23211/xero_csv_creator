from os import getenv
from re import search
from copy import deepcopy
from dotenv import load_dotenv
from operator import itemgetter
from datetime import datetime, timedelta

MAN_NUM_LENGTH = 7

class Invoice:
    def __init__(self, pricing):
        load_dotenv()
        self.invoice = [["*ContactName", "*InvoiceNumber", "Reference", "*InvoiceDate", "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "*AccountCode", "*TaxType"]]
        self.inv_date = '1/1/1990'
        self.inv_num = '-1'
        self.send_date = ''
        self.due_date = ''
        self.prices = pricing
        self.entered_man_nums = set()
    
    def set_date_num(self, date, num):
        self.inv_num = num
        self.inv_date = date
        self.send_date = datetime.strptime(self.inv_date, '%d/%m/%y')
        self.due_date = self.send_date + timedelta(days=30)

    def generate_fixed_info(self):
        return [
                getenv('CONTACT'), 
                self.inv_num.zfill(8),
                self.send_date.strftime('%d/%m/%y'),
                self.due_date.strftime('%d/%m/%y'),
                1,
                getenv('CODE'),
                getenv('TAX')
            ]

    def append_manifest(self, man_num, man_date, stores, loaded):
        if len(man_num) != MAN_NUM_LENGTH:
            raise Exception('Invalid manifest number')
        if man_num in self.entered_man_nums:
            raise Exception('Manifest number has already been entered')
        if len(stores) <= 0:
            raise Exception('No store numbers entered')
        
        try:
            loads = [self.prices[x.get()] for x in stores]
        except Exception as e:
            raise Exception(f'Store number {e} does not exist')

        loads.sort(key=itemgetter(2), reverse=True)
        for i in range(0, len(loads)):
            self.append_store(man_num, man_date, loads, i)

        if loaded:
            self.append_allowance()
            return len(loads) + 1
        return len(loads)

    def append_store(self, man_num, man_date, loads, i):
        #Add to set of current manifest numbers
        self.entered_man_nums.add(man_num)

        #Generate fixed columns
        row_to_add = self.generate_fixed_info()

        #Inventory Code
        row_to_add.insert(4, 'AD-PRIM' if i == 0 and man_num else 'DROP-RATE')

        #Description
        row_to_add.insert(5, f'{man_date} - {loads[i][0]} - {loads[i][1]}{f" - {man_num}" if i == 0 and man_num else ""}')

        #UnitAmount i.e. Price
        row_to_add.insert(7, loads[i][2] if i == 0 and man_num else '50')

        self.invoice.append(row_to_add)
    
    def append_allowance(self):
        allowance = self.generate_fixed_info()
        
        allowance.insert(4, self.prices['ALLWNCE'][0])
        allowance.insert(5, self.prices['ALLWNCE'][1])
        allowance.insert(7, self.prices['ALLWNCE'][2])

        self.invoice.append(allowance)

    def delete_manifest(self):
        if len(self.invoice) > 1:
            deleted_man_num = self.invoice.pop()[5][-MAN_NUM_LENGTH:]
            self.entered_man_nums.discard(deleted_man_num)
    
    def get_completed(self):
        complete = deepcopy(self.invoice)
        last_man_date = self.find_last_man(complete)
        for i in range(1, len(complete)):
            complete[i].insert(2, f"LOCAL: {self. get_inv_date()}-{last_man_date.group(0)}")
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
    
    def get_invoice(self):
        return self.invoice
    
    def get_inv_date(self):
        return self.inv_date