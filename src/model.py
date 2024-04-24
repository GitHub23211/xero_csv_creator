from csv import writer, QUOTE_MINIMAL
from tkinter import filedialog, messagebox
from data.loader import load_files, save_local_pricing

class Model:
    def __init__(self):
        self.pricings, self.invoice_info = self.load_pricings()

    def load_pricings(self):
        try:
            return load_files()
        except Exception as e:
            messagebox.showerror('Error', e)
    
    def update_pricing(self, pricing):
        save_local_pricing(pricing)
        self.pricings['LOCAL'] = pricing

    def save_csv(self, data):
        dir = filedialog.asksaveasfilename(initialdir='./', filetypes=[('CSV files', '*.csv')], defaultextension='.csv')
        with open(dir, mode='w', newline='') as csv_file:
            csv_writer = writer(csv_file, delimiter=",", quotechar='"', quoting=QUOTE_MINIMAL)
            csv_writer.writerows(data)
    
    def get_local_pricing(self):
        return self.pricings['LOCAL']
    
    def get_billing_pricing(self):
        return self.pricings['BILLING']

    def get_subbies_pricing(self):
        return self.pricings['SUBBIES']

    def get_rigid_pricing(self):
        return self.pricings['RIGID']
    
    def get_invoice_info(self):
        return self.invoice_info