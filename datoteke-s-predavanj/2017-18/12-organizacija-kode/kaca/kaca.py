import tkinter as tk
import model

VELIKOST_POLJA = 10
ODMIK = 5
ZACETNA_VELIKOST = (20, 20)

class Kaca:
    def __init__(self, okno):
        # Nastavimo model
        self.igra = model.Igra(*ZACETNA_VELIKOST)

        # Pripravimo grafični vmesnik
        self.okno = okno
        self.igralna_plosca = tk.Canvas(
            width=VELIKOST_POLJA * self.igra.sirina + 2 * ODMIK,
            height=VELIKOST_POLJA * self.igra.visina + 2 * ODMIK,
        )
        self.igralna_plosca.pack()
        self.okno.bind('<Key>', self.obdelaj_tipko)

        # Zaženemo osnovno zanko igre
        self.osnovna_zanka()

    def osnovna_zanka(self):
        self.igra.naredi_korak()
        self.osvezi_prikaz()
        self.okno.after(1000 // self.igra.tezavnost(), self.osnovna_zanka)

    def obdelaj_tipko(self, event):
        if event.keysym == 'Right':
            self.igra.kaca.zamenjaj_smer(model.DESNO)
        elif event.keysym == 'Left':
            self.igra.kaca.zamenjaj_smer(model.LEVO)
        elif event.keysym == 'Up':
            self.igra.kaca.zamenjaj_smer(model.GOR)
        elif event.keysym == 'Down':
            self.igra.kaca.zamenjaj_smer(model.DOL)

    def osvezi_prikaz(self):
        # Trenutno delamo tako, da vsakič vse pobrišemo in nato narišemo na novo.
        # TODO: To ni najbolje. V kratkem bomo naredili bolj skromno rešitev.
        self.igralna_plosca.delete('all')

        # Nariši okvir
        self.igralna_plosca.create_rectangle(
            ODMIK,
            ODMIK,
            int(self.igralna_plosca['width']) - ODMIK,
            int(self.igralna_plosca['height']) - ODMIK
        )

        # Nariši kačo, če je še zdrava
        if self.igra.je_kaca_v_redu():
            for x, y in self.igra.kaca.tocke:
                self.igralna_plosca.create_oval(
                    ODMIK + VELIKOST_POLJA * x,
                    ODMIK + VELIKOST_POLJA * y,
                    ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
                    ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA
                )

        # Nariši jabolko
        jabolko_x, jabolko_y = self.igra.jabolko
        self.igralna_plosca.create_oval(
            ODMIK + VELIKOST_POLJA * jabolko_x,
            ODMIK + VELIKOST_POLJA * jabolko_y,
            ODMIK + VELIKOST_POLJA * jabolko_x + VELIKOST_POLJA,
            ODMIK + VELIKOST_POLJA * jabolko_y + VELIKOST_POLJA,
            fill='green'
       )


okno = tk.Tk()
moj_program = Kaca(okno)
okno.mainloop()
