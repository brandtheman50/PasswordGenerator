import tkinter as tk
import random as rand
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("Password Generator")

#Window configuration
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(3, minsize=800, weight=1)

#Algorithm for complete random password

#Algorithm using hints for password

#Algorithm saving password to file

#Algorithm for deleting password from file

#Frames
fr_buttons = tk.Frame(window)
#Widgets and layouts
btn_show_pass = tk.Button(fr_buttons, text="Show Passwords")
btn_new_pass = tk.Button(fr_buttons, text="New Password")
btn_show_pass.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_new_pass.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
#Run window
window.mainloop()
