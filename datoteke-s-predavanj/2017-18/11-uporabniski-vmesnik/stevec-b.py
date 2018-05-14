import time
import tkinter as tk

def povecaj():
    vrednost_stevca = int(prikaz_vrednosti.cget('text'))
    prikaz_vrednosti.configure(text=str(vrednost_stevca + 1))

def resetiraj():
    prikaz_vrednosti.configure(text='0')

def zanka():
    povecaj()
    okno.after(100, zanka)

okno = tk.Tk()

okvir_za_gumbe = tk.Frame(okno)
gumb_povecaj = tk.Button(okvir_za_gumbe, text='+1', command=povecaj)
gumb_resetiraj = tk.Button(okvir_za_gumbe, text='RESET', command=resetiraj)
prikaz_vrednosti = tk.Label(okno, text='0', font=("Courier", 400))

prikaz_vrednosti.pack()
okvir_za_gumbe.pack()

gumb_povecaj.grid(row=0, column=0)
gumb_resetiraj.grid(row=0, column=1)

zanka()

okno.mainloop()
