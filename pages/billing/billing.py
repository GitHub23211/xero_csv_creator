from tkinter import Frame, Label, Entry, Button, StringVar, messagebox
from datetime import datetime, timedelta

from components import top
from pages.billing import b_ui

class Billing(top.Top):
    def __init__(self, root, model, width, height):
        top.Top.__init__(self, root, model, b_ui.billingUI, width, height)
        self.prices = self.model.billing['prices']
        self.emps = self.model.billing['emps']
        self.date_var = StringVar(value='')
        self.data = {}
        self.billing = None
        self.curr_view.build()

    def submit(self):
        try:
            self.model.save_billing(self.model.create_billing(self.data, self.date_var.get()))
        except Exception as e:
            messagebox.showerror('Error', f'Please enter a valid date {e}')

    def create_billing(self, data, date):
        try:
            bill_date = datetime.strptime(date, '%d/%m/%y')
            due_date = bill_date + timedelta(10)
            bills = []
            bills.extend(self.headings[0])
            for emp in data:
                emp_data = self.billing['emps'][emp]
                for load in data[emp]:
                    name = emp_data[0]
                    bill_ref = emp_data[1]
                    description = self.billing['prices'][load][0]
                    price = self.billing['prices'][load][1]
                    num_loads = data[emp][load].get() if data[emp][load].get() != '' else '0'
                    row_to_add = [name, bill_ref, bill_date.strftime('%d/%m/%y'), due_date.strftime('%d/%m/%y'), load, description, num_loads, price, '160', 'BAS Excluded']
                    bills.append(row_to_add)
            return bills
        except Exception as e:
            raise e