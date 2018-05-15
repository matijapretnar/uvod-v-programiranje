import tkinter as tk
import model

POLMER_TOCKE = 3

class DinamicnaGeometrija:
    def __init__(self):
        # Nastavimo model
        self.konstrukcija = model.Konstrukcija()
        self.obvestilo = ''

        # Pripravimo grafični vmesnik
        okno = tk.Tk()
        self.objekt_je_izbran = tk.BooleanVar()
        self.izbrani_objekt = None
        self.platno = tk.Canvas(okno)
        self.platno.pack(fill=tk.BOTH, expand=True)
        self.prikaz_obvestila = tk.Label(okno)
        self.prikaz_obvestila.pack(fill=tk.X)
        self.platno.bind('<Configure>', lambda event: self.osvezi_prikaz())

        okno.bind('P', self.dodaj_premico_skozi_dve_tocki)
        okno.bind('T', self.dodaj_prosto_tocko)
        okno.bind('X', self.dodaj_presecisce)
        okno.bind('<Escape>', self.razveljavi)
        okno.bind('<B1-Motion>', self.premakni_tocko)
        okno.mainloop()

    def premakni_tocko(self, event):
        self.izbrani_objekt.x = event.x
        self.izbrani_objekt.y = event.y
        self.osvezi_prikaz()

    def razveljavi(self, event):
        print('RAZVELJAVI')

    def izberi_objekt(self, obvestilo):
        self.objekt_je_izbran.set(False)
        self.obvestilo = obvestilo
        self.platno.wait_variable(self.objekt_je_izbran)
        self.obvestilo = ''
        return self.izbrani_objekt

    def izberi_novo_tocko(self, obvestilo):
        self.objekt_je_izbran.set(False)
        self.obvestilo = obvestilo
        def dodaj_tocko(event):
            self.izbrani_objekt = model.Tocka(event.x, event.y)
            self.objekt_je_izbran.set(True)
        self.platno.bind('<Button-1>', dodaj_tocko)
        self.platno.wait_variable(self.objekt_je_izbran)
        self.platno.unbind('<Button-1>')
        self.obvestilo = ''
        return self.izbrani_objekt

    def dodaj_prosto_tocko(self, event):
        self.konstrukcija.dodaj_tocko(self.izberi_novo_tocko('Izberite novo točko'))
        self.osvezi_prikaz()

    def dodaj_premico_skozi_dve_tocki(self, event):
        tocka1 = self.izberi_objekt('Izberite 1. točko')
        tocka2 = self.izberi_objekt('Izberite 2. točko')
        self.konstrukcija.dodaj_premico(model.PremicaSkoziTocki(tocka1, tocka2))
        self.osvezi_prikaz()

    def dodaj_presecisce(self, event):
        premica1 = self.izberi_objekt('Izberite 1. premico')
        premica2 = self.izberi_objekt('Izberite 2. premico')
        self.konstrukcija.dodaj_tocko(model.PreseciscePremic(premica1, premica2))
        self.osvezi_prikaz()

    def narisi_tocko(self, tocka):
        x, y = tocka.koordinate()
        slika_tocke = self.platno.create_oval(
            x - POLMER_TOCKE,
            y - POLMER_TOCKE,
            x + POLMER_TOCKE,
            y + POLMER_TOCKE,
            fill='white',
            activefill='blue',
            activeoutline='blue',
        )
        def izberi_tocko(event):
            self.izbrani_objekt = tocka
            self.objekt_je_izbran.set(True)
        self.platno.tag_bind(slika_tocke, '<Button-1>', izberi_tocko)

    def narisi_premico(self, premica):
        a, b, c = premica.parametri()
        x1 = 0
        y1 = (c - a * x1) / b
        x2 = self.platno.winfo_width()
        y2 = (c - a * x2) / b
        slika_premice = self.platno.create_line(
            x1,
            y1,
            x2,
            y2,
            activefill='blue',
        )
        def izberi_premico(event):
            self.izbrani_objekt = premica
            self.objekt_je_izbran.set(True)
        self.platno.tag_bind(slika_premice, '<Button-1>', izberi_premico)

    def osvezi_prikaz(self):
        self.platno.delete('all')

        # Nariši premice
        for premica in self.konstrukcija.premice:
            self.narisi_premico(premica)
            print(premica)

        # Nariši točke
        for tocka in self.konstrukcija.tocke:
            self.narisi_tocko(tocka)
            print(tocka)

        self.prikaz_obvestila.configure(text=self.obvestilo)


DinamicnaGeometrija()
