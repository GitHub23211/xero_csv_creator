import tkinter as tk
from atexit import register

from pages import home
import model
import state

if __name__ == '__main__':
    data = model.Model()
    root = tk.Tk()
    app_state = state.State(root, data)
    app = home.Home(app_state)
    register(data.cleanup)
    root.mainloop()
