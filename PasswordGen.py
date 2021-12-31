import tkinter as tk
import random as rand
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("Password Generator")

#Window configuration
window.rowconfigure(2, minsize=500, weight=1)
window.columnconfigure(3, minsize=600, weight=1)

#Algorithm for complete random password
def com_rand_password():
    return
    
#Algorithm using hints for password
def hints_rand_password():
    return

#Algorithm saving password to file
def save_password():
    return

#Function for showing passwords
def show_passwords():
    return

#Algorithm for deleting password from file
def delete_passwords():
    return

#Frames
first_row_buttons = tk.Frame(window)
fr_length = tk.Frame(window)
fr_random = tk.Frame(window)

#First Row Widgets
btn_show_pass = tk.Button(first_row_buttons, text="Show Passwords")
btn_new_pass = tk.Button(first_row_buttons, text="New Password")
btn_show_pass.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_new_pass.grid(row=1, column=0, sticky="ew", padx=5)
first_row_buttons.grid(row=0, column=0, sticky="ns")

#Second Row Widgets

#Length
lbl_length = tk.Label(fr_length, text="Length")
entry_length = tk.Entry(fr_length)
lbl_length.grid(row=0, column=0, padx=5, sticky="ew", pady=3)
entry_length.grid(row=1, column=0, padx=5, sticky="ew")

#Random Generate
lbl_random = tk.Label(fr_random, text="Generate completely random password")
btn_random_pass = tk.Button(fr_random, text="Generate", command=com_rand_password)
lbl_random.grid(row=0, column=0, sticky="ew", padx=5, pady=1)
btn_random_pass.grid(row=1, column=0, padx=5)

fr_length.grid(row=0, column=1, sticky="nsew")
fr_random.grid(row=1,column=1,sticky="nsew")
#Run window
window.mainloop()
