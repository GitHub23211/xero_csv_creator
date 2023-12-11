import tkinter as tk
from atexit import register

import model
from pages import home

if __name__ == '__main__':
    root = tk.Tk()
    app = home.Home(root)
    register(model.cleanup)
    root.mainloop()
