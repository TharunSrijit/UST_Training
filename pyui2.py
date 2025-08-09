import tkinter as tk
from tkinter import ttk,messagebox
import os.path
import csv

#main window
root = tk.Tk()
root.geometry("440x400")
root.title("Palindrome Check")
root.resizable(True, True)

def verify_user_entry(event):
    reverse_label.config(text="")
    if not event.char.isalnum():
        given_string_entry.delete(0, tk.END)
        given_string_entry.insert(0, given_string_entry.get()[:-1])

txt_file='PalindromeText.txt'
csv_file='ReversedTable.csv'

#create the palindromeText.txt file
if not os.path.exists(txt_file):
    with open(txt_file, 'w', newline='') as fp:
        fp.write('Palindrome List'+'\n'+'================'+'\n')

#create the reversedtable.csv file
if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(["Given", "Reversed"])

privilege = tk.IntVar()

pal_label=ttk.Label(root, text="Palindrome Check")
pal_label.grid(row=0, column=0,sticky=tk.W, columnspan=2, padx=20, pady=20)

admin_rdo_btn=ttk.Radiobutton(root, text="Administrator", variable=privilege, value=1)
admin_rdo_btn.grid(row=1, column=0, sticky=tk.W, padx=20, pady=20)

user_rdo_btn=ttk.Radiobutton(root, text="User", variable=privilege, value=0)
user_rdo_btn.grid(row=1, column=1, sticky=tk.W, padx=20, pady=20)

given_string_label = tk.Label(root, text="GIVEN STRING")
given_string_label.grid(column=0, row=2, sticky=tk.W,padx=5, pady=5)

given_string_entry = ttk.Entry(root)
given_string_entry.grid(column=1, row=2, sticky=tk.W,padx=5, pady=5)
given_string_entry.bind('<KeyRelease>', verify_user_entry)

reverse_btn = tk.Button(root, text="REVERSE", command="")
reverse_btn.grid(column=2, row=2, sticky=tk.W,padx=5, pady=5)

result_label = tk.Label(root, text="REVERESED STRING:")
result_label.grid(column=0, row=3, sticky=tk.W,padx=5, pady=5)

reverse_label = tk.Label(root, text="",font='helvetica 100 bold')
reverse_label.grid(column=1, row=3, sticky=tk.W,padx=5, pady=5,columnspan=3)

root.mainloop()