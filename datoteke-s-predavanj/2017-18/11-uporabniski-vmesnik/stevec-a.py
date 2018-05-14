import tkinter as tk

class Stevec:
    def __init__(self):
        self.vrednost = 0
        self.zgodovina = []

    def povecaj(self):
        self.shrani_zgodovino()
        self.vrednost += 1

    def zmanjsaj(self):
        self.shrani_zgodovino()
        self.vrednost -= 1

    def shrani_zgodovino(self):
        self.zgodovina.append(self.vrednost)

    def razveljavi(self):
        self.vrednost = self.zgodovina.pop()

    def ponastavi(self):
        self.shrani_zgodovino()
        self.vrednost = 0

#################################################################################################

stevec = Stevec()

def dogodek_povecaj():
    stevec.povecaj()
    osvezi_prikaz()

def dogodek_ponastavi():
    stevec.ponastavi()
    osvezi_prikaz()

def dogodek_zmanjsaj():
    stevec.zmanjsaj()
    osvezi_prikaz()

def dogodek_razveljavi():
    stevec.razveljavi()
    osvezi_prikaz()

def osvezi_prikaz():
    if stevec.zgodovina:
        gumb_razveljavi.configure(state=tk.NORMAL)
    else:
        gumb_razveljavi.configure(state=tk.DISABLED)
    prikaz_vrednosti.configure(text=str(stevec.vrednost))



okno = tk.Tk()

okvir_za_gumbe = tk.Frame(okno)
gumb_povecaj = tk.Button(okvir_za_gumbe, text='+1', command=dogodek_povecaj)
gumb_zmanjsaj = tk.Button(okvir_za_gumbe, text='-1', command=dogodek_zmanjsaj)
gumb_ponastavi = tk.Button(okvir_za_gumbe, text='RESET', command=dogodek_ponastavi)
gumb_razveljavi = tk.Button(okvir_za_gumbe, text='UNDO', command=dogodek_razveljavi)
prikaz_vrednosti = tk.Label(okno, font=("Courier", 400))
osvezi_prikaz()

prikaz_vrednosti.pack()
okvir_za_gumbe.pack()

gumb_povecaj.grid(row=0, column=0)
gumb_zmanjsaj.grid(row=0, column=1)
gumb_ponastavi.grid(row=0, column=2)
gumb_razveljavi.grid(row=0, column=3)

okno.mainloop()
