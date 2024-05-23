from datetime import datetime, timedelta
from copy import deepcopy

class RigidInvoice():
    def __init__(self, inv_info):
        self.invoice = [["*ContactName", "*InvoiceNumber", "Reference", "*InvoiceDate", "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "*AccountCode", "*TaxType"]]
        self.fixed_info = inv_info

    def generate_fixed_info(self, inv_num, inv_date):
        send_date = datetime.strptime(inv_date, '%d/%m/%y')
        due_date = send_date + timedelta(days=30)
        return [
                self.fixed_info['CONTACT'], 
                inv_num.zfill(8),
                send_date.strftime('%d/%m/%y'),
                due_date.strftime('%d/%m/%y'),
                self.fixed_info['CODE'],
                self.fixed_info['TAX']
            ]

    def create_rigid_invoice(self, inv_date, inv_num, rigid_stores):
        invoice = deepcopy(self.invoice)
        for key, store in rigid_stores.items():
        #Generate fixed columns
            row_to_add = self.generate_fixed_info(inv_num, inv_date)

            #Reference
            row_to_add.insert(2, self.determine_reference(key, inv_date))

            #Inventory Code
            row_to_add.insert(5, store['code'])

            #Description
            row_to_add.insert(6, store['description'])

            #Quantity
            row_to_add.insert(7, store['quantity'].get())

            #UnitAmount i.e. Price
            row_to_add.insert(8, store['price'])

            invoice.append(row_to_add)
        return invoice
    
    def determine_reference(self, store, inv_date):
        start = datetime.strptime(inv_date, '%d/%m/%y')
        end = start + timedelta(days=6)
        period = f'{start.strftime('%d/%m')} - {end.strftime('%d/%m/%y')}'
        if store:
            if store in ('187', '60'):
                return f'BOND&LANE: {period}'
            elif store in ('113', '110', '103'):
                return f'MON&DY&NTHS: {period}'
            elif store in ('114'):
                return f'MOS: {period}'
            else:
                return f'TOUR 1 - 6: {period}'