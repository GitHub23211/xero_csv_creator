import tkinter as tk
import main

height = 700
width = 300

window = tk.Tk()
window.minsize(width, height)
window.title("Xero Invoice Creator")

#Invoice Number
frame_1 = tk.Frame(window)
frame_1.grid(row=0, column=0, sticky="w")

date_lbl = tk.Label(master=frame_1, text="Invoice Date")
num_lbl = tk.Label(master=frame_1, text="Invoice Number")
date_lbl.grid(row=0, column=0)
num_lbl.grid(row=0, column=1)

date_ent = tk.Entry(master=frame_1)
num_ent = tk.Entry(master=frame_1)
date_ent.grid(row=1, column=0)
num_ent.grid(row=1, column=1)

# Manifest Info frame
frame_2 = tk.Frame(window)
frame_2.grid(row=1, column=0)

mandate_lbl = tk.Label(master=frame_2, text="Manifest Date")
manno_lbl = tk.Label(master=frame_2, text="Manifest Number")

mandate_lbl.grid(row=0, column=0)
manno_lbl.grid(row=0, column=1)

mandate_ent = tk.Entry(master=frame_2)
manno_ent = tk.Entry(master=frame_2)
mandate_ent.grid(row=1, column=0)
manno_ent.grid(row=1, column=1)

# Load input
frame_3 = tk.Frame(window)
frame_3.grid(row=2, column=0, sticky="w")

strno_lbl = tk.Label(master=frame_3, text="Store Number")
strno_lbl.grid(row=0, column=0)

load_info = []
for i in range(1, 4):
    strno_ent = tk.Entry(master=frame_3)
    strno_ent.grid(row=i, column=0)
    load_info.append(strno_ent)

add_ent = tk.Button(master=frame_3, text="Add Manifest", command=lambda : main.add_manifest(load_info, num_ent.get(), mandate_ent.get(), date_ent.get(), manno_ent.get()))
add_ent.grid(row=4, column=0, sticky="w")

#Added manifests


window.mainloop()