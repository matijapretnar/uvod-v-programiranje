import pickle
import tkinter as tk
import tkinter.filedialog as filedialog
import model

class GeoGebrica:
    def __init__(self):
        okno = tk.Tk()

        # Nastavimo model
        self.objekti = []
        self.obvestilo = ''
        self.objekt_je_izbran = tk.BooleanVar()
        self.izbrani_objekt = None

        # Pripravimo meni
        glavni_meni = tk.Menu(okno)
        okno.config(menu=glavni_meni)

        meni_datoteka = tk.Menu(glavni_meni)
        glavni_meni.add_cascade(label='Datoteka', menu=meni_datoteka)
        meni_konstrukcija = tk.Menu(glavni_meni)
        glavni_meni.add_cascade(label='Konstrukcija', menu=meni_konstrukcija)

        meni_datoteka.add_command(label='Odpri', command=self.odpri)
        meni_datoteka.add_command(label='Shrani', command=self.shrani)
        meni_datoteka.add_separator()
        meni_datoteka.add_command(label='Izhod', command=None)

        meni_konstrukcija.add_command(label='Prosta točka', command=self.dodaj_prosto_tocko)
        meni_konstrukcija.add_command(label='Premica skozi dve točki', command=self.dodaj_premico_skozi_dve_tocki)
        meni_konstrukcija.add_command(label='Krožnica skozi dve točki', command=self.dodaj_kroznico_skozi_dve_tocki)
        meni_konstrukcija.add_command(label='Vzporednica', command=self.dodaj_vzporednico)
        meni_konstrukcija.add_command(label='Pravokotnica', command=self.dodaj_pravokotnico)
        meni_konstrukcija.add_command(label='Presečišče', command=self.dodaj_presecisce)

        # Pripravimo uporabniški vmesnik
        self.platno = tk.Canvas(okno)
        self.platno.pack(fill=tk.BOTH, expand=True)
        self.prikaz_obvestila = tk.Label(okno)
        self.prikaz_obvestila.pack(fill=tk.X)
        self.platno.bind('<Configure>', lambda event: self.osvezi_prikaz())

        # Nastavimo bližnjice
        okno.bind('P', self.dodaj_premico_skozi_dve_tocki)
        okno.bind('K', self.dodaj_kroznico_skozi_dve_tocki)
        okno.bind('T', self.dodaj_prosto_tocko)
        okno.bind('V', self.dodaj_vzporednico)
        okno.bind('p', self.dodaj_pravokotnico)
        okno.bind('X', self.dodaj_presecisce)
        okno.bind('<B1-Motion>', self.premakni_tocko)

        # Poženemo glavno zanko
        okno.mainloop()

    def shrani(self):
        ime_datoteke = filedialog.asksaveasfilename()
        with open(ime_datoteke, 'wb') as datoteka:
            pickle.dump(self.objekti, datoteka)

    def odpri(self):
        ime_datoteke = filedialog.askopenfilename()
        with open(ime_datoteke, 'rb') as datoteka:
            self.objekti = pickle.load(datoteka)
        self.osvezi_prikaz()

    def narisi_objekt(self, objekt):
        def izberi_objekt(event):
            self.izbrani_objekt = objekt
            self.objekt_je_izbran.set(True)
        slika_objekta = objekt.slika_na_platnu(self.platno)
        self.platno.tag_bind(slika_objekta, '<Button-1>', izberi_objekt)

    def osvezi_prikaz(self):
        self.platno.delete('all')
        for objekt in self.objekti:
            self.narisi_objekt(objekt)
        self.prikaz_obvestila.configure(text=self.obvestilo)

    def premakni_tocko(self, event):
        self.izbrani_objekt.x = event.x
        self.izbrani_objekt.y = event.y
        self.osvezi_prikaz()

    def izberi_objekt(self, vrsta, obvestilo):
        self.obvestilo = obvestilo
        self.izbrani_objekt = None
        self.osvezi_prikaz()
        while not isinstance(self.izbrani_objekt, vrsta):
            self.izbrani_objekt = None
            self.objekt_je_izbran.set(False)
            self.platno.wait_variable(self.objekt_je_izbran)
        self.obvestilo = ''
        return self.izbrani_objekt

    def dodaj_tocko(self, tocka):
        self.objekti.append(tocka)
        self.osvezi_prikaz()

    def dodaj_kroznico(self, kroznica):
        self.objekti.insert(0, kroznica)
        self.osvezi_prikaz()

    def dodaj_premico(self, premica):
        self.objekti.insert(0, premica)
        self.osvezi_prikaz()

    def dodaj_prosto_tocko(self, *args):
        def dodaj_tocko(event):
            self.izbrani_objekt = model.Tocka(event.x, event.y)
            self.objekt_je_izbran.set(True)
        self.platno.bind('<Button-1>', dodaj_tocko)
        self.dodaj_tocko(self.izberi_objekt(model.Tocka, 'Izberite novo točko'))
        self.platno.unbind('<Button-1>')

    def dodaj_premico_skozi_dve_tocki(self, *args):
        tocka1 = self.izberi_objekt(model.Tocka, 'Izberite 1. točko')
        tocka2 = self.izberi_objekt(model.Tocka, 'Izberite 2. točko')
        self.dodaj_premico(model.PremicaSkoziTocki(tocka1, tocka2))

    def dodaj_kroznico_skozi_dve_tocki(self, *args):
        tocka1 = self.izberi_objekt(model.Tocka, 'Izberite 1. točko')
        tocka2 = self.izberi_objekt(model.Tocka, 'Izberite 2. točko')
        self.dodaj_kroznico(model.KroznicaSkoziTocki(tocka1, tocka2))

    def dodaj_presecisce(self, *args):
        premica1 = self.izberi_objekt(model.Premica, 'Izberite 1. premico')
        premica2 = self.izberi_objekt(model.Premica, 'Izberite 2. premico')
        self.dodaj_tocko(model.PreseciscePremic(premica1, premica2))

    def dodaj_pravokotnico(self, *args):
        premica = self.izberi_objekt(model.Premica, 'Izberite premico')
        tocka = self.izberi_objekt(model.Tocka, 'Izberite točko')
        self.dodaj_premico(model.Pravokotnica(premica, tocka))

    def dodaj_vzporednico(self, *args):
        premica = self.izberi_objekt(model.Premica, 'Izberite premico')
        tocka = self.izberi_objekt(model.Tocka, 'Izberite točko')
        self.dodaj_premico(model.Vzporednica(premica, tocka))


GeoGebrica()
