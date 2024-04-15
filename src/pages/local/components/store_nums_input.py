from tkinter import Frame, Entry, Button, Label, Checkbutton, BooleanVar

class StoreNumsInput:
    def __init__(self, root, commands):
        self.root = root
        self.store_nums = []
        self.commands = commands
        self.loaded = BooleanVar(value=False)
    
    def get_store_nums(self):
        return self.store_nums

    def get_loaded(self):
        return self.loaded.get()

    def reset_store_nums(self):
        for i in range(0, 3):
            self.store_nums[i].delete(0, 'end')

    def reset_loaded(self):
        self.loaded.set(False)
    
    def checkbox(self, f):
        loaded_checkbox = Checkbutton(f, text='Loaded by driver?', variable=self.loaded, takefocus=0)
        loaded_checkbox.grid(row=1, column=1)

    def store_num_ent(self, f):
        Label(f, text="Store Number").grid(row=1, column=0)

        for i in range(2, 5):
            str_no_ent = Entry(f)
            str_no_ent.grid(row=i, column=0)
            self.store_nums.append(str_no_ent)

    def buttons(self, f):
        add_ent_btn = Button(f, text="Add Manifest", command=self.commands['add'], takefocus=0)
        add_ent_btn.grid(row=2, column=1, padx=20, sticky=('e', 'w'))

        del_ent_btn = Button(f, text="Delete Last Entry", command=self.commands['delete'], takefocus=0)
        del_ent_btn.grid(row=3, column=1, padx=20, sticky=('e', 'w'))

        save_csv_btn = Button(f, text='Save CSV', command=self.commands['save'], takefocus=0)
        save_csv_btn.grid(row=4, column=1, padx=20, sticky=('e', 'w'))
    
    def build(self):
        f = Frame(self.root)
        f.grid(pady=10)
        self.checkbox(f)
        self.store_num_ent(f)
        self.buttons(f)



    
