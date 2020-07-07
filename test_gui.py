from tkinter import *
root = Tk()

v = StringVar()
e = Entry(root, textvariable=v)
e.pack()

v.set("a default value")
s = v.get()

root.mainloop()