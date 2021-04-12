---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Tekstovni vmesnik

Za primer večjega programa v Pythonu bomo napisali enostaven program, ki nam bo omogočal beleženje opravil. Običajno je naš prvi instinkt, da poženemo urejevalnik kode in začnemo gledati, kako bi nastavili barvo gumbov. Vendar ta način običajno vodi v zmedeno kodo in posledično tudi neuporaben vmesnik, ki ga je zelo težko spreminjati. Zato se moramo stvari lotiti v pravem vrstnem redu in prvi korak je, da zapremo urejevalnik kode.

## Skica vmesnika

Nato na papir (ali na tablico) skiciramo, kaj pričakujemo od našega programa. Kakšen vmesnik bo ponujal, kam bodo izbire vodile uporabnika, … Ni treba, da je skica preveč natančna, važno je le, da na njej zajamemo vse, kar si v danem trenutku predstavljamo. Risanje je hitro in poceni, zato ni nič hudega, če s skico zgrešimo, saj jo vedno lahko popravimo. Primer skice, ki je nastala pred začetkom pisanja našega programa je:

![](slike/skica-vmesnika.png)

## Skica modela

Tudi ko bo skica končana, se še ne bomo lotili pisanja vmesnika. Bolj pomembno je, da ugotovimo, kaj je naš _model_, torej predstavitev podatkov, s katerimi bomo delali. Če najprej model napišemo dobro, bo nudil trdno osnovo vmesniku (kot bomo videli celo več vmesnikom). Če pa se najprej lotimo vmesnika, bodo podatki zmešani z vmesnikom in ob prehodu na drug vmesnik (na primer iz tekstovnega na spletnega) bomo morali spremeniti veliko kode. Pri določitvi modela moramo ugotoviti, kaj so osnovni podatki, s katerimi želimo delati, in kakšne operacije bodo podpirali. Ker je Python objektni jezik, bomo vsako vrsto podatkov predstavili s svojim razredom. Pri določanju tega, katere atribute in metode mora vsebovati, nam bo v pomoč skica vmesnika.

![](slike/skica-modela.png)

Na skici označimo, katere razrede bomo imeli. Ker bomo beležili opravila, bomo vsekakor potrebovali razred `Opravilo`. Opravila bomo združevali v seznamih (domača opravila, službena opravila, …), katerih razred bomo poimenovali `Spisek`, da ne bo zmede s Pythonovimi seznami. Na koncu pa bomo potrebovali še razred, ki bo zajemal vse podatke, ki jih potrebujemo. Temu razredu lahko rečemo kar `Model`. Vsak izmed razredov bo imel določene atribute, ki jih napišemo na vrhu, ter metode, ki jih napišemo na dnu. Povezav med razredi ne bomo pisali pod atribute, temveč jih bomo označili s povezavami na diagramu. Na vsaki povezavi si tudi zapišemo, koliko objektov je povezanih med seboj. Na primer, model ima lahko več spiskov, vendar le en aktualni spisek. Spisek ima en model in več opravil.

## Implementacija modela

Na osnovi spiska zapišemo definicije ustreznih razredov. Najbolje, da kar v datoteko `model.py`. Ker bomo imeli opravka z roki opravil, si bomo pomagali z vgrajeno knjižnico [`datetime`](https://docs.python.org/3/library/datetime.html), ki med drugim ponuja razreda `date` za delo z datumi ter `timedelta` za časovna obdobja (ki jih bomo potrebovali za ponavljajoča se opravila). Ko bomo implementirali metode, bomo opazili, da naša skica ni bila popolna (metod za popravljanje podatkov ne bomo rabili, na opravilih pa nam manjka metoda za ugotavljanje, ali je rok zamujen). Nič hudega, saj za skico nismo porabili preveč časa.

```{code-cell} ipython3
from datetime import date

class Model:
    def __init__(self):
        self.spiski = []
        self.aktualni_spisek = None
    
    def dodaj_spisek(self, spisek):
        self.spiski = spisek
        if not self.aktualni_spisek:
            self.aktualni_spisek = spisek
    
    def pobrisi_spisek(self, indeks):
        self.spiski.pop(indeks)
    
    def zamenjaj_spisek(self, indeks):
        self.aktualni_spisek = self.spiski[indeks]

class Spisek:
    def __init__(self, ime):
        self.ime = ime
        self.opravila = []
    
    def dodaj_opravilo(self, ime, opis, rok, ponovitev):
        opravilo = Opravilo(self, ime, opis, rok, ponovitev)
        self.opravila.append(opravilo)
    
    def pobrisi_opravilo(self, indeks):
        self.opravila.pop(indeks)
    
    def stevilo_cez_rok(self):
        # Python bo True samodejno pretvoril v 1, False pa v 0        
        return sum([opravilo.cez_rok() for opravilo in self.opravila])

class Opravilo:
    def __init__(self, spisek, ime, opis, rok, ponovitev):
        self.spisek = spisek
        self.ime = ime
        self.opis = opis
        self.rok = rok
        self.ponovitev = ponovitev
        self.opravljeno = None
    
    def cez_rok(self):
        return self.rok and not self.opravljeno and self.rok < date.today()
    
    def opravi(self):
        self.opravljeno = date.today()
        if self.ponovitev:
            self.spisek.dodaj_opravilo(
                self.ime,
                self.opis,
                self.rok + self.ponovitev,
                self.ponovitev
            )
```

## Implementacija vmesnika

Ko je model v osnovi napisan, se lahko lotimo vmesnika. Za začetek se bomo lotili tekstovnega vmesnika, ki bo uporabniku izpisal trenutni prikaz ter s konzole prebral njegova navodila. Da bomo dobro poskrbeli za ločitev od modela, bomo vmesnik napisali v ločeno datoteko `tekstovni_vmesnik.py`. Paziti moramo, da iz vmesnika do modela dostopamo prek metod, saj bo tako celotno vedenje definirano v `model.py`. Prav tako je treba paziti, da iz modela nikoli ne dostopamo do vmesnika. To enostavno preprečimo tako, da se v `model.py` nikoli ne skličemo na datoteko `tekstovni_vmesnik.py`. Ker sta obe datoteki v istem imeniku, lahko model uvozimo kar kot:

```python
from model import Model

model = Model()
```

Za začetek bo naš model prazen, kmalu pa si bomo pogledali, kako ga shranimo v datoteko in kasneje preberemo nazaj. Pisanja vmesnika se lotimo _od zgoraj navzdol_. Začnemo z osnovno zanko, ki bo pokazala pozdravno sporočilo, nato pa v nedogled uporabniku ponujala osnovni zaslon. Zato bo osnovna funkcija sledeča:

```python
def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        osnovni_zaslon()
```

Osnovni zaslon bo najprej pokazal aktualna opravila, nato pa prebral ukaz in odvisno od njega poklical naslednjo funkcijo:

```python
DODAJ_OPRAVILO = 'dodaj'
OPRAVI_OPRAVILO = 'opravi'

def osnovni_zaslon():
    prikazi_aktualna_opravila()
    ukaz = preberi_ukaz()
    if ukaz == DODAJ_OPRAVILO:
        dodaj_opravilo()
    elif ukaz == OPRAVI_OPRAVILO:
        opravi_opravilo()
    ...
```

Vsak ukaz bomo predstavili s svojim nizom. Da se ne bomo zatipkali in npr. v funkciji `osnovni_zaslon` pisali `'dodaj'`, v funkciji `preberi_ukaz` pa `'Dodaj'`, bomo ukaze shranili v konstante, ki so običajne spremenljivke, vendar s samimi velikimi črkami označujemo, da njihovih vrednosti ne bomo spreminjali. Če se bomo zatipkali pri pisanju imena konstante, nas bo na to opozoril urejevalnik.

Funkcije bomo tako drobili naprej, na ustreznih točkah pa bomo poklicali metode na modelu. Na primer:

```python
def dodaj_opravilo():
    ime = input('Ime opravila> ')
    ...
    model.aktualni_spisek.dodaj_opravilo(ime, ...)
```

## Shranjevanje stanja

Da ne bomo ob zaprtju programa izgubili vseh podatkov, si jih bomo pred zaprtjem shranili v datoteko, ki jo bomo ob vsakem zagonu prebrali. Tako bo naš vmesnik sledeče oblike:

```python
from model import Model

IME_DATOTEKE = 'stanje.json'
model = Model.preberi_iz_datoteke(IME_DATOTEKE)

...

def osnovni_zaslon():
    while True:
        ...
        elif ukaz == ZAKLJUCI:
            model.shrani_v_datoteko(IME_DATOTEKE)
            print('Nasvidenje!')
            break         
```

Da ne bomo izumljali tople vode, si bomo stanje zapisali v JSON datoteko. Ker Python našega modela ne zna samodejno spremeniti v JSON, bomo sami napisali vmesno pretvorbo v slovar. Vse naše objekte moramo tako dopolniti z metodami za pretvorbo v slovar in iz slovarja. Prve bodo običajne metode, ki bodo vrnile slovar, na primer:

```python
class Spisek:
    ...
    
    def v_slovar(self):
        return {
            'ime': self.ime,
            'opravila': [opravilo.v_slovar() for opravilo in self.opravila]
        }

class Opravilo:
    ...
    
    def v_slovar(self):
        return {
            'ime': self.ime,
            'opis': self.opis,
            'rok': niz_datuma(self.rok),
            'ponovitev': niz_obdobja(self.ponovitev) if self.ponovitev else None,
            'opravljeno': niz_datuma(self.opravljeno) if self.opravljeno else None
        }
```

Kot vidimo, v slovarju spiska nastopajo opravila, obratno pa ne, saj bi sicer dobili ciklično strukturo, ki je ne moremo pametno zapisati v slovar.

Metode za pretvorbo iz slovarja pa so malo bolj posebne, saj pred trenutnkom, ko preberemo slovar, še nimamo objekta, na katerih bi jih poklicali. Lahko bi si sicer napisali funkcije kot so `preberi_opravilo_iz_slovarja` ali `preberi_spisek_iz_slovarja`, vendar te funkcije zelo naravno spadajo v ustrezne razrede. Hkrati pa niso metode, saj nimajo objekta, na katerih jih lahko pokličemo. Gre za _statične metode_, ki so v resnici navadne funkcije, le da jih kot metode zapišemo v razred in na vrhu označimo s `@staticmethod` (v resnici bi bilo boljša možnost `@classmethod`, ampak o tem kdaj drugič):

```python
class Spisek:
    ...
    
    @staticmethod
    def iz_slovarja(slovar):
        spisek = Spisek(slovar['ime'])
        spisek.opravila = [Opravilo.iz_slovarja(spisek, sl_opravila) for sl_opravila in slovar['opravila']]
        return spisek

class Opravilo:
    ...
    
    @staticmethod
    def iz_slovarja(spisek, slovar):
        return Opravilo(
            spisek,
            slovar['ime'],
            slovar['opis'],
            datum_niza(slovar['rok']),
            obdobje_niza(slovar['ponovitev']) if slovar['ponovitev'] else None,
            datum_niza(slovar['opravljeno']) if slovar['opravljeno'] else None,            
        )
```

V statični metodi `iz_slovarja` moramo posebej navesti spisek, na katerem naj bo opravilo, saj tega v slovarju nismo posebej zabeležili.

Opremljeni z vsemi funkcijami lahko shranjevanje in nalaganje modela napišemo kot:

```python
import json

class Model:
    ...
    
    def shrani(self, ime_datoteke):
        with open(ime_datoteke, 'w') as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)
    
    @staticmethod
    def nalozi(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Model.iz_slovarja(slovar)
