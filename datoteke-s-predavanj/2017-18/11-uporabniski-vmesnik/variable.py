import tkinter as tk

def prezrcali(*args):
    obrnjen_niz_var.set(niz_var.get()[::-1])

okno = tk.Tk()

niz_var = tk.StringVar()
obrnjen_niz_var = tk.StringVar()

vhod = tk.Entry(okno, textvariable=niz_var, font=("Courier", 50))
izhod = tk.Label(okno, textvariable=obrnjen_niz_var, font=("Courier", 50))
niz_var.trace('w', prezrcali)

vhod.pack()
izhod.pack()

okno.mainloop()
