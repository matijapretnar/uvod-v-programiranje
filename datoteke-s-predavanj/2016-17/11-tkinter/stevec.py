import tkinter as tk

def povecaj():
    prikaz_stevca.configure(text=vnosno_polje.get())

def ponastavi():
    print(vnosno_polje.get())

def pomanjsaj():
    print('Zmanjšujem za 1')

okno = tk.Tk()

vnosno_polje = tk.Entry(okno)
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
vnosno_polje.pack()

okno.mainloop()
