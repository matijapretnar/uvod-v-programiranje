import tkinter as tk

def kvadriraj(*args):
    kvadrat_var.set(stevilo_var.get() ** 2)
okno = tk.Tk()
stevilo_var = tk.DoubleVar()
stevilo_var.trace('w', kvadriraj)
kvadrat_var = tk.DoubleVar()
vhod = tk.Entry(okno, textvariable=stevilo_var)
vhod.pack()
izhod = tk.Label(okno, textvariable=kvadrat_var)
izhod.pack()
okno.mainloop()