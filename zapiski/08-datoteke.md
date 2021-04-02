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

# Datoteke

## Branje datotek

Recimo, da imamo datoteko `stavki.txt` s sledečo vsebino:

```
To je prvi stavek. To je drugi
stavek. To je tretji stavek. To
je četrti stavek.
```

Če vsebino želimo prebrati, moramo datoteko najprej odpreti. To storimo s funkcijo `open`. Klicu `open` lahko podamo tudi neobvezni argument `encoding`, ki poda kodno tabelo, v kateri je napisana datoteka. Težava je, da je privzeta vrednost parametra na Windowsih `cp1250`, kar je precej zastarel standard, zato morate tam pisati `open(..., encoding='UTF-8')`.

```{code-cell} ipython3
dat = open('stavki.txt', encoding='UTF-8')
dat
```

Dobili smo objekt `dat`, ki predstavlja dostop do vsebine datoteke. Najosnovnejša metoda je `read`, ki ob vsakem klicu prebere dano število znakov.

```{code-cell} ipython3
dat.read(35)
```

```{code-cell} ipython3
dat.read(20)
```

Če števila ne podamo, datoteko preberemo do konca:

```{code-cell} ipython3
dat.read()
```

```{code-cell} ipython3
dat.read()
```

Datoteko je treba po koncu uporabe treba zapreti, da lahko do nje dostopajo tudi drugi programi. Se vam je kdaj zgodilo, da USB ključka niste mogli varno odstraniti, ker naj bi ga uporabljal še nek program? Težava je bila, da slabo napisan program ni zaprli dostopa do datotek, zato je operacijski sistem mislil, da jih še vedno uporablja. Datotetko lahko zapremo z metodo `close`.

```{code-cell} ipython3
dat.close()
```

Da ne pozabimo zapreti datoteke, ali pa da nam zapiranja ne prepreči napaka v programu, Python ponuja varnejši način odpiranja datotek. Če napišemo

```python
with open('stavki.txt') as dat:
    ...
```

bo Python samodejno poskrbel za zapiranje datoteke, ko se bodo izvedli vsi stavki `...`. To bo veljalo tudi v primeru, če kakšen izmed stavkov sproži izjemo in prekine izvajanje.
 
Za branje po vrsticah lahko uporabimo metodi `readline` in `readlines`:

```{code-cell} ipython3
with open('stavki.txt') as dat:
    prva = dat.readline()
    druga = dat.readline()
    ostale = dat.readlines()
```

```{code-cell} ipython3
prva
```

```{code-cell} ipython3
druga
```

```{code-cell} ipython3
ostale
```

Po vrsticah se lahko zapeljemo z zanko `for`:

```{code-cell} ipython3
with open('stavki.txt') as dat:
    for vrstica in dat:
        print(len(vrstica), vrstica)
```

Vidimo, da so med izpisanimi vrsticami tudi prazne. Te so posledice tega, da vsaka vrstica datoteke na koncu vsebuje znak za novo vrstico, en tak znak pa doda še `print`.

```{code-cell} ipython3
def izpisi_datoteko(ime_datoteke):
    print(ime_datoteke)
    with open(ime_datoteke) as dat:
        for st_vrstice, vrstica in enumerate(dat, 1):
            print(st_vrstice, vrstica, end='')
```

```{code-cell} ipython3
izpisi_datoteko('stavki.txt')
```

## Pisanje datotek

Datoteke lahko tudi pišemo, vendar jih moramo ustrezno odpreti, kar naredimo kot:
Na Windowsih, kjer je treba podat

```python
with open(..., 'w') as d:
    ...
```

oziroma


```python
with open(..., 'w', encoding='UTF-8') as d:
    ...
```

Ko datoteko odpremo za pisanje, lahko vanjo pišemo z metodo `write`

```{code-cell} ipython3
with open('izpis.txt', 'w') as dat:
    dat.write('To je ')
    dat.write('en stavek.\nTo je drugi.')
```

```{code-cell} ipython3
izpisi_datoteko('izpis.txt')
```

V datoteko pišemo tudi s `print`, ki mu podamo neobvezni argument `file`:

```{code-cell} ipython3
with open('izpis.txt', 'w') as dat:
    print('To je en stavek.', file=dat)
    print('1 + 1 =', 1 + 1, file=dat)
```

```{code-cell} ipython3
izpisi_datoteko('izpis.txt')
```

Vsakič, ko datoteko odpremo za pisanje, povozimo obstoječo vsebino:

```{code-cell} ipython3
with open('izpis.txt', 'w') as dat:
    print('To je en stavek.', file=dat)
    print('To je drugi.', file=dat)
```

```{code-cell} ipython3
with open('izpis.txt', 'w') as dat:
    print('To je tretji stavek.', file=dat)
    print('To je četrti.', file=dat)
```

```{code-cell} ipython3
izpisi_datoteko('izpis.txt')
```

Če želimo, lahko namesto `w` podamo parameter `a`, ki datoteko odpremo za dodajanje:

```{code-cell} ipython3
with open('izpis.txt', 'w') as d:
    print('To je en stavek.', file=d)
    print('To je drugi.', file=d)
```

```{code-cell} ipython3
with open('izpis.txt', 'a') as d:
    print('To je tretji stavek.', file=d)
    print('To je četrti.', file=d)
```

```{code-cell} ipython3
izpisi_datoteko('izpis.txt')
```

## Delo z datotečnim sistemom


Tako, kot si daljše programe shranjujemo v datoteke, si tudi večje količine podatkov shranimo v datoteke. Poglejmo si najprej, kako so datoteke na računalniku sploh organizirane. Vsak nosilec podatkov (trdi disk, SSD, DVD, USB ključek) ima podatke zapisane v določenem datotečnem sistemu, ki je odvisen od vrste nosilca in operacijskega sistema. Na primer, trdi diski pod Windowsi so običajno formatirani v sistemu NTFS, pod Linuxom v sistemu Ext, na Macintoshu pa v sistemu HFS. USB ključki so zaradi lažje prenosljivosti ponavadi vsi formatirani v sistemu FAT (ki se je včasih uporabljal pod Windowsi). Če želimo, lahko na nosilcu naredimo več particij in vsako od njih ločeno formatiramo s svojim datotečnim sistemom.

Datotečni sistem določa, v kakšni obliki je na nosilcu shranjena vsebina datotek in v kakšni obliki je predstavljena uporabniku. S prvim se ne bomo ukvarjali, pri drugem pa je pomembna le razlika med operacijskim sistemom Windows in sistemi, osnovanimi na UNIXu (torej Linux ali OS X).

Datotečni sistem vsebuje datoteke, razporejene po mapah (oz. direktorijih), ki so lahko tudi gnezdene. Na vrhu imamo korensko mapo, ki jo v operacijskih sistemih, osnovanih na UNIXu, označujemo z `/`, na operacijskem sistemu Windows pa z `C:\`, kjer je `C` ime particije: `C` običajno označuje glavni pogon, `D` drugi pogon ali CD/DVD/BlueRay enoto, `A` in `B` sta se uporabljali za diskete, kasnejše črke pa se uporabljajo za USB ključke in podobno.

Za primer vzemimo datotečni sistem s sledečimi mapami in datotekami:

+++

```
/
    uvp
        datoteke
            vhodna.txt
            izhodna.txt
        funkcije.py
        seznami.py
        slovarji.py
        zanke.py
    praktikum
        latex
            pismo.tex
            pismo.pdf
            pismo.aux
        mathematica
            grafi.nb
            kolokvij.nb
    analiza
        plonkec.tex
```

+++

Vsaka datoteka ima absolutno pot, na kateri jo lahko najdemo. Na primer absolutna pot datoteke `pismo.tex` je `/praktikum/latex/pismo.tex` oz. `C:\praktikum\latex\pismo.tex` na Windowsih. Do datotek kaže tudi relativna pot. Na primer, glede na imenik `praktikum` je pot do `pismo.tex` kar `latex/pismo.tex`. Če želimo, gremo z `..` tudi ven iz trenutnega imenika. Na primer, glede na imenik `mathematica` je relativna pot do `vhodna.txt` enaka `../../uvp/datoteke/vhodna.txt`.

+++

Za delo z datotečnim sistemom je na voljo knjižnica `os`:

```{code-cell} ipython3
import os
```

Trenutni imenik dobimo z `os.getcwd`:

```{code-cell} ipython3
os.getcwd()
```

zamenjamo pa ga z `os.chdir`, ki sprejme absolutno ali relativno pot:

```{code-cell} ipython3
os.chdir('..')
os.getcwd()
```

```{code-cell} ipython3
os.chdir('zapiski')
os.getcwd()
```

Imena vseh datotek v danem imeniku dobimo z `os.listdir`:

```{code-cell} ipython3
os.listdir()
```

```{code-cell} ipython3
os.listdir('slike')
```

Vse funkcije za delo z datotekami lahko najdete v [uradni dokumentaciji], ostale pogosto uporabljene pa so:

- `os.mkdir(pot)`, ki naredi imenik z dano potjo.
- `os.makedirs(pot, exist_ok=False)`, ki naredi imenik z dano potjo in vse vmesne imenike. Če je argument `exist_ok` nastavljen na `True`, ne javi napake, če ciljna mapa že obstaja.
- `os.rename(stara_pot, nova_pot)` datoteko ali imenik s potjo `stara_pot` preimenuje v `nova_pot`.
- `os.remove(pot)` pobriše datoteko z dano potjo.
- `os.rmdir(pot)` pobriše imenik z dano potjo.
- `os.removedirs(pot)` pobriše imenik z dano potjo in vse vmesne imenike.

+++

Poleg knjižnice `os` je na voljo tudi knjižnica `os.path` za delo z datotečnimi potmi:

+++

- `os.path.join(pot1, pot2)` stakni poti `pot1` in `pot2`, pri čemer ustrezno poskrbi za prava ločila glede na operacijski sistem.
- `os.path.isdir(pot)` vrne `True`, kadar `pot` vodi do imenika.
- `os.path.exists(pot)` vrne `True`, kadar `pot` obstaja v datotečnem sistemu.
- `os.path.splitext(pot)` loči pot datoteke na del pred končnico in del za njo:

```{code-cell} ipython3
os.path.splitext('/imenik/podimenik/test.txt')
```

- `os.path.split(pot)` loči na pot do zadnje imenika in na ime datoteke.  Do prve komponente lahko dostopamo tudi z `os.path.dirname(pot)`, do druge pa z metodo `os.path.basename(pot)`.

```{code-cell} ipython3
os.path.split('/imenik/podimenik/test.txt')
```

```{code-cell} ipython3
os.path.dirname('/imenik/podimenik/test.txt')
```

```{code-cell} ipython3
os.path.basename('/imenik/podimenik/test.txt')
```

- `os.path.abspath(pot)` dano pot pretvori v absolutno:

```{code-cell} ipython3
os.path.abspath('../02-rekurzija/')
```

## JSON datoteke

Za zapis strukturiranih podatkov je uveljavljen standard [JSON](https://www.json.org/json-sl.html), ki ga podpirajo skoraj vsa orodja za delo s podatki. Vrednosti v njem so lahko:
- števila,
- logični vrednosti `true` in `false` (pozorni bodite na malo začetnico),
- nizi (ki jih obvezno pišemo med narekovaje `"`),
- ničelna vrednost `null` (ki igra enako vlogo kot `None`),
- seznami (ki jih pišemo enako kot v Pythonu) ter
- objekti (ki so podobno kot slovarji v Pythonu, le da so ključi lahko le nizi).

Na primer:

```json
{
  "ime": "Anka Cvetnik",
  "vpisnaStevilka": 27123456,
  "visina": 167.8,
  "prijatelji": [27154321, 27165432],
  "predmetnik": [
    {"predmet": "Analiza 1", "ocena": 10},
    {"predmet": "Algebra 1", "ocena": 10},
    {
      "predmet": "Uvod v programiranje",
      "ocena": null
    }
  ]
}
```

V Pythonu je delu z JSONom namenjena knjižnica `json`. Najenostavnejša funkcija v njej je `loads`, ki prebere niz z JSONom in vrne ustrezno Pythonovo vrednost:

```{code-cell} ipython3
import json
json.loads('[1, {"3": true, "4": null}]')
```

V obratno smer deluje funkcija `json.dumps`, ki Pythonovo vrednost pretvori v JSON:

```{code-cell} ipython3
>>> json.dumps([1, {3: True, 4: None}])
'[1, {"3": true, "4": null}]'
```

Vidimo, da je funkcija ključe slovarjev tudi ustrezno spremenila v nize.

Če želimo delati z JSON datotekami, imamo na voljo funkcijo `dump`, ki poleg vrednosti sprejme datoteko, v katero naj zapiše JSON vrednost.

```{code-cell} ipython3
with open('primer.json', 'w') as dat:
    json.dump([1, {3: True, 4: None}], dat)
```

```{code-cell} ipython3
izpisi_datoteko('primer.json')
```

Če želimo, lahko datoteko tudi lepo oblikujemo z zamiki: 

```{code-cell} ipython3
with open('primer.json', 'w') as dat:
    json.dump([1, {3: True, 4: None}], dat, indent=4)
```

```{code-cell} ipython3
izpisi_datoteko('primer.json')
```

Podobno obstaja funkcija `load`, ki datoteko prebere:

```{code-cell} ipython3
with open('primer.json') as datoteka:
    vrednost = json.load(datoteka)
vrednost
```
