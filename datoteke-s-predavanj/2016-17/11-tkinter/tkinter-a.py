import tkinter as tk

def povecaj():
    trenutna_vrednost = int(prikaz_stevca['text'])
    prikaz_stevca.configure(text=str(trenutna_vrednost + 1))

def ponastavi():
    prikaz_stevca.configure(text='0')

def pomanjsaj():
    trenutna_vrednost = int(prikaz_stevca['text'])
    prikaz_stevca.configure(text=str(trenutna_vrednost - 1))

okno = tk.Tk()

gumbi = tk.Frame(okno)
gumb_povecaj = tk.Button(gumbi, text='+1', command=povecaj)
gumb_pomanjsaj = tk.Button(gumbi, text='-1', command=pomanjsaj)
gumb_ponastavi = tk.Button(gumbi, text='0', command=ponastavi)
prikaz_stevca = tk.Label(okno, text='0')

gumb_povecaj.grid(row=0, column=2)
gumb_ponastavi.grid(row=0, column=1)
gumb_pomanjsaj.grid(row=0, column=0)
prikaz_stevca.pack()
gumbi.pack()

okno.mainloop()
