import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

file = "readme.md"


def select_file():
    global file

    cwd = os.getcwd
    file_types = [
        ("Text files", "*.txt"),
        ("Markdown files", "*.md"),
        ("All files", "*.*"),
    ]

    file = filedialog.askopenfilename(
        title="Select a file", initialdir=cwd, filetypes=file_types
    )


def compress():
    global file
    chars = count_chars(file)  # sorted dictionary in descending order

    try:
        for char, count in chars.items():
            print(f"{char}: {count}")
    except AttributeError:
        print(chars)


def count_chars(file):
    chars = {}  # Dictionary - char: instances
    try:
        # Saves the selected file in 'f' var.
        # This allow us to work with the file within this block
        # The file will automatically close when the blocks end
        with open(file, "r") as f:
            for char in f.read():  # f.read() is the string of the entire file content
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1  # Insert the item with key 'char' and 'value' 1

        # Sorts 'chars' dictionary in descending order
        return dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    except FileNotFoundError:
        return "File not found"


def gui():
    root = tk.Tk()
    root.title("Huffman Compression Tool")
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    frm.config(
        width=300,
        height=300,
    )
    frm.pack()
    ttk.Button(frm, text="Select File ", command=select_file).grid(column=0, row=0)
    ttk.Button(frm, text="Compress", command=compress).grid(column=0, row=10)
    ttk.Button(frm, text="Decompress").grid(column=0, row=15)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=20)
    root.mainloop()


gui()
