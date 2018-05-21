import tkinter as tk
import model

class SemaforVmesnik:
    def __init__(self):
        self.semafor = model.SemaforModel()
        okno = tk.Tk()
        self.luc = tk.Canvas(okno, width=100, height=100)
        gumb_zelena = tk.Button(okno, command=self.daj_na_zeleno, text='zelena')
        gumb_rumena = tk.Button(okno, command=self.daj_na_rumeno, text='rumena')
        gumb_rdeca = tk.Button(okno, command=self.daj_na_rdeco, text='rdeča')
        self.luc.pack()
        gumb_zelena.pack()
        gumb_rumena.pack()
        gumb_rdeca.pack()
        self.osvezi_prikaz()
        okno.mainloop()

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
            model.RDECA: 'red',
            model.RUMENA: 'yellow',
            model.ZELENA: 'green',
        }
        self.luc.delete('all')
        self.luc.create_oval(0, 0, 100, 100, fill=ime_tkinter_barve[self.semafor.barva])

SemaforVmesnik()
