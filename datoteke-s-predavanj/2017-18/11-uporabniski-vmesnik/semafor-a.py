import tkinter as tk

RDECA, ZELENA, RUMENA = 'rdeca', 'zelena', 'rumena'

class SemaforModel:
    def __init__(self):
        self.barva = RDECA

    def daj_na_zeleno(self):
        self.barva = ZELENA

    def daj_na_rumeno(self):
        self.barva = RUMENA

    def daj_na_rdeco(self):
        self.barva = RDECA


class SemaforVmesnik:
    def __init__(self):
        self.semafor = SemaforModel()
        self.okno = tk.Tk()
        self.luc = tk.Canvas(self.okno, width=100, height=100)
        gumb_zelena = tk.Button(self.okno, command=self.daj_na_zeleno, text='zelena')
        gumb_rumena = tk.Button(self.okno, command=self.daj_na_rumeno, text='rumena')
        gumb_rdeca = tk.Button(self.okno, command=self.daj_na_rdeco, text='rdeča')
        self.luc.pack()
        gumb_zelena.pack()
        gumb_rumena.pack()
        gumb_rdeca.pack()
        self.osvezi_prikaz()
        # okno.mainloop()

    def daj_na_zeleno(self):
        self.semafor.daj_na_zeleno()
        self.osvezi_prikaz()

    def daj_na_rumeno(self):
        self.semafor.daj_na_rumeno()
        self.osvezi_prikaz()

    def daj_na_rdeco(self):
        self.semafor.daj_na_rdeco()
        self.osvezi_prikaz()

    def osvezi_prikaz(self):
        ime_tkinter_barve = {
            RDECA: 'red',
            RUMENA: 'yellow',
            ZELENA: 'green',
        }
        self.luc.delete('all')
        self.luc.create_oval(0, 0, 100, 100, fill=ime_tkinter_barve[self.semafor.barva])

SemaforVmesnik()
