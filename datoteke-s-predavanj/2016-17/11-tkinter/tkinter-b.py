import tkinter as tk

class MojSuperStevec:
    def __init__(self, okno):
        self.stevec = 0
        self.pripravi_graficni_vmesnik(okno)

    def pripravi_graficni_vmesnik(self, okno):
        prikaz = tk.Frame(okno)
        prikaz.grid(row=0, column=0)
        self.prikaz_stevca = tk.Label(prikaz)
        self.osvezi_prikaz()
        self.prikaz_stevca.pack()

        gumbi = tk.Frame(okno)
        gumbi.grid(row=1, column=0)
        povecaj_gumb = tk.Button(gumbi, text='+1', command=self.povecaj)
        povecaj_gumb.grid(row=0, column=0)
        ponastavi_gumb = tk.Button(gumbi, text='0', command=self.ponastavi)
        ponastavi_gumb.grid(row=0, column=1)
        pomanjsaj_gumb = tk.Button(gumbi, text='-1', command=self.pomanjsaj)
        pomanjsaj_gumb.grid(row=0, column=2)

    def povecaj(self):
        self.stevec += 1
        self.osvezi_prikaz()

    def pomanjsaj(self):
        self.stevec -= 1
        self.osvezi_prikaz()

    def ponastavi(self):
        self.stevec = 0
        self.osvezi_prikaz()

    def osvezi_prikaz(self):
        self.prikaz_stevca['text'] = str(self.stevec)


okno = tk.Tk()
okno1 = tk.Tk()
okno2 = tk.Tk()
moj_program = MojSuperStevec(okno)
moj_program = MojSuperStevec(okno1)
moj_program = MojSuperStevec(okno2)
okno.mainloop()
