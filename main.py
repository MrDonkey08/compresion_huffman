from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import locale

locale.setlocale(locale.LC_ALL, 'spanish')

def read():
    cwd = os.getcwd
    file_type=[('Files TXT', '*.txt')]
    filed = filedialog.askopenfilename(initialdir=cwd, filetypes=file_type)

    f = open(filed, "r")

    print(f.readline())

    #readline.read_init_file([filed])

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
frm.config(width=300, height=300, )
frm.pack()
ttk.Button(frm, text='Load File', command=read).grid(column=0, row=0)
ttk.Button(frm, text="Compress").grid(column=0, row=5)
ttk.Button(frm, text="Decompress").grid(column=0, row=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=20)
root.mainloop()