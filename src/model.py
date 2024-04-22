from csv import writer, QUOTE_MINIMAL
from json import load, dump

from tkinter import filedialog

class Model:
    def __init__(self):
        self.json_files = [open('./billing.json', mode='r'), open('./store_pricing.json', mode='r')]
        self.billing = load(self.json_files[0])
        self.pricing = load(self.json_files[1])
        self.cleanup()

    def save_csv(self, data):
        dir = filedialog.asksaveasfilename(initialdir='./', filetypes=[('CSV files', '*.csv')], defaultextension='.csv')
        csv_file = open(dir, mode='w', newline='')
        csv_writer = writer(csv_file, delimiter=",", quotechar='"', quoting=QUOTE_MINIMAL)
        csv_writer.writerows(data)
        csv_file.close()
    
    def update_pricing(self, pricing):
        self.pricing = pricing
        with open('./store_pricing.json', 'w') as fp:
            dump(self.pricing, fp, indent=4)

    def cleanup(self):
        for file in self.json_files:
            file.close()