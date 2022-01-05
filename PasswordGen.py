import tkinter as tk
import random as rand
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("Password Generator")

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "!@#$%^&*()_+-=,./?><"

lowercase_length = 25
uppercase_length = 25
all_numbers = 9
special_chars_num = len(special_chars) - 1

#Window configuration
window.rowconfigure(6, minsize=150, weight=1)
window.columnconfigure(3, minsize=600, weight=1)

#Function to check if user input valid length
# region 
def validate_length():
    if entry_length.get() and entry_length.get().isnumeric():
        length = int(entry_length.get())
        if (length > 7) and (length < 256):
            com_rand_password()
    else:
        return
# endregion

#Function to check if user input valid length and at least one hint
def validate_length_hints():
    if entry_length.get() and entry_length.get().isnumeric():
        length = int(entry_length.get())
        if (length > 7) and (length < 256):
            if entry_hint1.get() or entry_hint2.get() or entry_hint3.get():
                hints_rand_password()
    else:
        return

def validate_password(password):
    valid_upper = False
    valid_num = False
    valid_symbol = False

    if checked_upper_box:
        for c in password:
            if c.isupper():
                valid_upper = True
                break
    else:
        valid_upper = True
    
    if checked_num_box:
        for c in password:
            if c.isdigit():
                valid_num = True
    else:
        valid_num = True

    if checked_symbol_box:    
        if any(c in special_chars for c in password):
            valid_symbol = True
    else:
        valid_symbol = True
    if valid_upper and valid_num and valid_symbol:
        return True
    else:
        return False
    
    
#Algorithm for complete random password
# region 
def com_rand_password():
    entry_password.delete(0, tk.END)
    password = ""
    length = int(entry_length.get())
    for i in range(0,length):
        rand_type = rand.randint(1,4)
        #Random lowercase letter
        if rand_type == 1:
            rand_char = rand.randint(0,25)
            new_char = lowercase[rand_char]
        #Random uppercase letter
        elif rand_type == 2:
            rand_char = rand.randint(0,25)
            new_char = uppercase[rand_char]
        #Random number
        elif rand_type == 3:
            rand_num = rand.randint(0,9)
            new_char = numbers[rand_num]
        #Random special character
        else:
            rand_num = rand.randint(0, special_chars_num)
            new_char = special_chars[rand_num]
        password = password + new_char
    if validate_password(password):
        entry_password.insert(0, password)
    else:
        com_rand_password()
# endregion

    
#Algorithm using hints for password
def hints_rand_password():
    
    return

#Algorithm saving password to file
def save_password():
    if entry_password.get() and entry_site.get() and entry_username.get():
        file = open("SavedPasswords.txt", "a")
        get_password = "Password: " + entry_password.get() + "\n" 
        get_site = "Website: " + entry_site.get() + "\n"
        get_username = "Username: " + entry_username.get() + "\n"

        L = [get_site, get_username, get_password]
        file.writelines(L)
        file.write("\n")
        file.close()

#Function for showing saved passwords
def show_passwords():
    return

#Algorithm for deleting password from file
def delete_passwords():
    return

#Frames
# region 
first_row_buttons = tk.Frame(window)
fr_checkboxes = tk.Frame(window)
fr_length = tk.Frame(window)
fr_random = tk.Frame(window)
fr_hint1 = tk.Frame(window)
fr_hint2 = tk.Frame(window)
fr_hint3 = tk.Frame(window)
fr_hints_btn = tk.Frame(window)
fr_password = tk.Frame(window)
fr_save_pass = tk.Frame(window)
# endregion

#First Column Widgets
# region 
btn_show_pass = tk.Button(first_row_buttons, text="Show Passwords")
btn_new_pass = tk.Button(first_row_buttons, text="New Password")
btn_show_pass.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_new_pass.grid(row=1, column=0, sticky="ew", padx=5)
first_row_buttons.grid(row=0, column=0, sticky="ns")
# endregion
#Second Column Widgets

#Requirements boxes
# region 
checked_upper_box = tk.BooleanVar(value=False)
checked_num_box = tk.BooleanVar(value=False)
checked_symbol_box = tk.BooleanVar(value=False)

check_uppercase = tk.Checkbutton(fr_checkboxes, text='Uppercase', variable = checked_upper_box, onvalue=True, offvalue=False)
check_number = tk.Checkbutton(fr_checkboxes, text="Number", variable=checked_num_box, onvalue=True, offvalue=False)
check_symbol = tk.Checkbutton(fr_checkboxes, text="Symbol", variable=checked_symbol_box, onvalue=True, offvalue=False)
check_uppercase.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
check_number.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
check_symbol.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

fr_checkboxes.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
# endregion

#Length
# region 
lbl_length = tk.Label(fr_length, text="Length")
entry_length = tk.Entry(fr_length, width=5)
lbl_length.grid(row=0, column=0, padx=5, sticky="ew", pady=3)
entry_length.grid(row=1, column=0, padx=5, sticky="ew")

fr_length.grid(row=1, column=1, sticky="nsew")
# endregion

#Random Generate
# region 
lbl_random = tk.Label(fr_random, text="Generate completely random password")
btn_random_pass = tk.Button(fr_random, text="Generate", command=validate_length)
lbl_random.grid(row=0, column=0, sticky="ew", padx=5, pady=1)
btn_random_pass.grid(row=1, column=0, padx=5, pady=5)

fr_random.grid(row=2,column=1,sticky="nsew")
# endregion

#Hint 1 Widgets
lbl_hint1 = tk.Label(fr_hint1, text="Hint 1")
entry_hint1 = tk.Entry(fr_hint1)
lbl_hint1.grid(row=0, column=0, sticky="ew", padx=5, pady=3)
entry_hint1.grid(row=1, column="0", sticky="ew", padx=5,)

fr_hint1.grid(row=3, column=1, sticky="nsew")

#Hint 2 Widgets
lbl_hint2 = tk.Label(fr_hint2, text="Hint 2")
entry_hint2 = tk.Entry(fr_hint2)
lbl_hint2.grid(row=0, column=0, sticky="ew", padx=5, pady=3)
entry_hint2.grid(row=1, column="0", sticky="ew", padx=5,)

fr_hint2.grid(row=4, column=1, sticky="nsew")

#Hint 3 Widgets
lbl_hint3 = tk.Label(fr_hint3, text="Hint 3")
entry_hint3 = tk.Entry(fr_hint3)
lbl_hint3.grid(row=0, column=0, sticky="ew", padx=5, pady=3)
entry_hint3.grid(row=1, column="0", sticky="ew", padx=5,)

fr_hint3.grid(row=5, column=1, sticky="nsew")

#Button using hints
btn_hints_pass = tk.Button(fr_hints_btn, text="Generate Using Hints", command=validate_length_hints)
btn_hints_pass.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

fr_hints_btn.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

#Password Generator
entry_password = tk.Entry(fr_password)
entry_password.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

fr_password.grid(row=4, column=3, sticky="nsew")

#Save Password Button Frame
lbl_site = tk.Label(fr_save_pass, text="Site")
lbl_username = tk.Label(fr_save_pass, text="Username")
entry_site = tk.Entry(fr_save_pass)
entry_username = tk.Entry(fr_save_pass)
lbl_site.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
entry_site.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
lbl_username.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
entry_username.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

btn_save_pass = tk.Button(fr_save_pass, text="Save Password", command=save_password)
btn_save_pass.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

fr_save_pass.grid(row=5, column=3, sticky="nsew")
#Run window
window.mainloop()
