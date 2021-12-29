import tkinter as tk
window = tk.Tk()

# Code to add widgets will go here...
greeting = tk.Label(
    text="Password Generator",
    fg="blue",      #Foreground - color of text
    bg="#14C1D3",   #Background - color of background
    width=50,       #Size measured in text units
    height=5)      

hint1 = tk.Label(
    text="Hint",
)

entry = tk.Entry()

hintGet = entry.get()


greeting.pack()
hint1.pack()
entry.pack()






#Run window
window.mainloop()
window.destroy()