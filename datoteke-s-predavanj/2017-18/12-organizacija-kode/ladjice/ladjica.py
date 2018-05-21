import tkinter as tk
import model

class PotapljanjeLadjic:
    def __init__(self, okno):
        self.plosca = model.Plosca(10, 10)

        self.obvestilo = tk.Label(okno, text='Pozdravljen v potapljanju ladjic!')
        self.obvestilo.grid(row=0, column=0)

        self.stevec_potez = tk.Label(okno, text='0')
        self.stevec_potez.grid(row=0, column=1)

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        for vrstica in range(self.plosca.visina):
            vrstica_gumbov = []
            for stolpec in range(self.plosca.sirina):
                def pritisni_gumb(vrstica=vrstica, stolpec=stolpec):
                    self.izstreli(vrstica, stolpec)
                gumb = tk.Button(prikaz_plosce, text='', height=1, width=1, command=pritisni_gumb)
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.grid(row=1, column=0, columnspan=2)


    def izstreli(self, vrstica, stolpec):
        rezultat = self.plosca.izstreli_izstrelek(vrstica, stolpec)

        if rezultat == model.ZADETA:
            self.gumbi[vrstica][stolpec].config(text='x', state='disabled')
            self.obvestilo.config(text='Zadel si ladjo!')

        elif rezultat == model.ZGRESENA:
            self.gumbi[vrstica][stolpec].config(text='o', state='disabled')
            self.obvestilo.config(text='Zgrešil si ladjo!')

        elif rezultat == model.KONEC_IGRE:
            for vrstica_gumbov in self.gumbi:
                for gumb in vrstica_gumbov:
                    gumb.config(state='disabled')
            self.obvestilo.config(text='POTOPIL SI VSE LADJICE!')

        self.stevec_potez.config(text=str(self.plosca.poteze))



okno = tk.Tk()
moj_stevec = PotapljanjeLadjic(okno)
okno.mainloop()
