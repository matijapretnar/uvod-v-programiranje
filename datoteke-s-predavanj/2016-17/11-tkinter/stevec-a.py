import tkinter as tk

class MojStevec:
    def __init__(self, okno):
        gumbi = tk.Frame(okno)
        self.gumb_povecaj = tk.Button(gumbi, text='+1', command=self.povecaj)
        gumb_pomanjsaj = tk.Button(gumbi, text='-1', command=self.pomanjsaj)
        gumb_ponastavi = tk.Button(gumbi, text='0', command=self.ponastavi)
        gumb_shrani = tk.Button(okno, text='SHRANI', command=self.shrani_nastavitve) 
        self.prikaz_stevca = tk.Label(okno, text='0')

        self.gumb_povecaj.grid(row=0, column=2)
        gumb_ponastavi.grid(row=0, column=1)
        gumb_pomanjsaj.grid(row=0, column=0)
        self.prikaz_stevca.pack()
        gumb_shrani.pack()
        gumbi.pack()

        self.datoteka_z_nastavitvami = 'nastavitve.txt'
        self.nalozi_nastavitve()
        self.osvezi_prikaz()


    def osvezi_prikaz(self):
        self.prikaz_stevca.configure(text=str(self.stevec))

        if self.stevec <= 9:
            self.gumb_povecaj.config(state='normal')
        else:
            self.gumb_povecaj.config(state='disabled')
        
    def povecaj(self):
        self.stevec += 1
        self.osvezi_prikaz()

    def ponastavi(self):
        self.stevec = 0
        self.osvezi_prikaz()

    def pomanjsaj(self):
        self.stevec -= 1
        self.osvezi_prikaz()

    def nalozi_nastavitve(self):
        try:
            with open(self.datoteka_z_nastavitvami) as datoteka:
                self.stevec = int(datoteka.read())
        except:
            self.stevec = 0
        self.osvezi_prikaz()

    def shrani_nastavitve(self):
        with open(self.datoteka_z_nastavitvami, 'w') as datoteka:
            datoteka.write(str(self.stevec))

okno = tk.Tk()
moj_stevec = MojStevec(okno)
okno.mainloop()
