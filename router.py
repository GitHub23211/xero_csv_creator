def change_view(old, new, root):
    old.destroy()
    new(root)