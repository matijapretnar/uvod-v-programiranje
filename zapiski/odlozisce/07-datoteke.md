# Datoteke

## Odpiranje datotek

`stavki.txt`

```
To je prvi stavek. To je drugi
stavek. To je tretji stavek. To
je četrti stavek.
```

Kaj izpiše spodnji ukaz?

```
>>> print('stavki.txt')
```

Datoteko **za branje odpremo** s funkcijo `open`

```
>>> open('stavki.txt')
<_io.TextIOWrapper name='stavki.txt'
 mode='r' encoding='UTF-8'>
```

Z `read` preberemo **dano število znakov**

```
>>> dat = open('stavki.txt')
>>> dat.read(35)
'To je prvi stavek. To je drugi\nstav'
>>> dat.read(20)
'ek. To je tretji sta'
>>> dat.read()
'vek. To\nje četrti stavek.\n'
>>> dat.read()
''
```

Z `readline` preberemo **naslednjo vrstico**

```
>>> dat = open('stavki.txt')
>>> dat.readline()
'To je prvi stavek. To je drugi\n'
>>> dat.readline()
'stavek. To je tretji stavek. To\n'
>>> dat.readline()
'je četrti stavek.\n'
>>> dat.readline()
''
```

Z `readlines` preberemo **vse vrstice**

```
>>> dat = open('stavki.txt')
>>> dat.readlines()
['To je prvi stavek. To je drugi\n',
 'stavek. To je tretji stavek. To\n',
 'je četrti stavek.\n']
```

Po vrsticah se lahko **zapeljemo z zanko** `for`

```
>>> dat = open('stavki.txt')
>>> for vrstica in dat:
...     print(len(vrstica), vrstica)
...
*31 To je prvi stavek. To je drugi
*
*32 stavek. To je tretji stavek. To
*
*18 je četrti stavek.
```

Datoteko je po uporabi **dobro zapreti**

```
dat = open('ime_datoteke.txt')
...
dat.close()
```

Namesto tega **raje pišemo**

```
with open('ime_datoteke.txt') as dat:
    ...
```

Število vrstic, znakov in besed v slovenskih klasikih

Naključno generirani slovenski klasiki

Kodno tabelo nastavimo s **parametrom `encoding`**

```
with open(..., encoding='utf-8') as d:
    ...
```

```
with open(..., encoding='cp1250') as d:
    ...
```

```
with open(..., encoding='latin2') as d:
    ...
```

Datoteko za **pisanje** odpremo s parametrom `w`

```
with open(..., 'w') as d:
    ...
```

## Metode na datotekah

V datoteko pišemo z metodo `write`

```
with open('izpis.txt', 'w') as d:
    d.write('To je ')
    d.write('en stavek.\nTo je drugi.')
```

`izpis.txt`

```
To je en stavek.
To je drugi.
```

V datoteko pišemo tudi s `print`

```
with open('izpis.txt', 'w') as d:
    print('To je en stavek.', file=d)
    print('1 + 1 =', 1 + 1, file=d)
```

`izpis.txt`

```
To je en stavek
1 + 1 = 2
```

Vsakič, ko datoteko odpremo za pisanje, jo **povozimo**

```
with open('izpis.txt', 'w') as d:
    print('To je en stavek.', file=d)
    print('To je drugi.', file=d)
```

`izpis.txt`

```
To je en stavek.
To je drugi.
```

```
with open('izpis.txt', 'w') as d:
    print('To je tretji stavek.', file=d)
    print('To je četrti.', file=d)
```

`izpis.txt`

```
To je tretji stavek.
To je četrti.
```

Datoteko **za dodajanje** odpremo s parametrom `a`

```
with open('izpis.txt', 'a') as d:
    print('To je en stavek.', file=d)
    print('To je drugi.', file=d)
```

`izpis.txt`

```
To je en stavek.
To je drugi.
```

Datoteko **za dodajanje** odpremo s parametrom `a`

```
with open('izpis.txt', 'a') as d:
    print('To je tretji stavek.', file=d)
    print('To je četrti.', file=d)
```

`izpis.txt`

```
To je en stavek.
To je drugi.
To je tretji stavek.
To je četrti.
```

Oštevilčene vrstice slovenskih klasikov

## Delo z datotečnim sistemom

ečni sistem

Tako, kot si daljše programe shranjujemo v datoteke, si tudi večje količine podatkov shranimo v datoteke. Poglejmo si najprej, kako so datoteke na računalniku sploh organizirane. Vsak nosilec podatkov (trdi disk, SSD, DVD, USB ključek) ima podatke zapisane v določenem datotečnem sistemu, ki je odvisen od vrste nosilca in operacijskega sistema. Na primer, trdi diski pod Windowsi so običajno formatirani v sistemu NTFS, pod Linuxom v sistemu Ext, na Macintoshu pa v sistemu HFS. USB ključki so zaradi lažje prenosljivosti ponavadi vsi formatirani v sistemu FAT (ki se je včasih uporabljal pod Windowsi). Če želimo, lahko na nosilcu naredimo več particij in vsako od njih ločeno formatiramo s svojim datotečnim sistemom.

Datotečni sistem določa, v kakšni obliki je na nosilcu shranjena vsebina datotek in v kakšni obliki je predstavljena uporabniku. S prvim se ne bomo ukvarjali, pri drugem pa je pomembna le razlika med operacijskim sistemom Windows in sistemi, osnovanimi na UNIXu (torej Linux ali OS X).

Datotečni sistem vsebuje datoteke, razporejene po mapah (oz. direktorijih), ki so lahko tudi gnezdene. Na vrhu imamo korensko mapo, ki jo v operacijskih sistemih, osnovanih na UNIXu, označujemo z `/`, na operacijskem sistemu Windows pa z `C:\`, kjer je `C` ime particije: `C` običajno označuje glavni pogon, `D` drugi pogon ali CD/DVD/BlueRay enoto, `A` in `B` sta se uporabljali za diskete, kasnejše črke pa se uporabljajo za USB ključke in podobno.

Za primer vzemimo datotečni sistem s sledečimi mapami in datotekami:

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

```
/uvp/datoteke/vhodna.txt
```

Na Windowsih je zadeva malo drugačna

```
C:\uvp\datoteke\vhodna.txt
```

Do datotek kaže tudi **relativna pot**, odvisna od trenutnega imenika

```
../latex/pismo.tex
```

- `os.listdir(pot)`

  : Vrne imena vseh datotek v mapi s potjo `pot`.

- `os.path.jon(pot1, pot2)`

  : Stakne poti `pot1` in `pot2`, pri čemer ustrezno poskrbi za

  ```
  prava ločila glede na operacijski sistem.
  ```

- `os.path.isdir(pot)`

  : Vrne `True`, kadar `pot` vodi do mape.

- `os.path.exists(pot)`

  : Vrne `True`, kadar `pot` obstaja v datotečnem sistemu.

- `os.path.splitext(pot)`

  : Večina datotek ima končnico, ki se začne z znakom `.` in

  ```
  označuje tip datoteke (`.jpg` za JPEG slike, `.docx` za Wordove
  dokumente, ...). Metoda dano `pot` loči na del pred končnico in
  na končnico.
  ```

- `os.path.split(pot)`

  : Dano pot loči na pot do zadnje mape in na ime datoteke. Do prve

  ```
  komponente lahko dostopamo tudi z metodo `os.path.dirname(pot)`,
  do druge pa z metodo `os.path.basename(pot)`.
  ```

- `os.mkdir(pot)`

  : Naredi mapo z dano potjo.

- `os.makedirs(pot, exist_ok=False)`

  : Naredi mapo z dano potjo in vse vmesne imenike. Če je argument

  ```
  `exist_ok` nastavljen na `True`, ne javi napake, če ciljna mapa
  že obstaja.
  ```

- `os.rename(stara_pot, nova_pot)`

  : Datoteko ali mapo s potjo `stara_pot` preimenuje v `nova_pot`.

- `os.remove(pot)`

  : Pobriše datoteko z dano potjo.

- `os.rmdir(pot)`

  : Pobriše mapo z dano potjo.

- `os.removedirs(pot)`

  : Pobriše mapo z dano potjo in vse vmesne imenike.

- `os.path.normpath(pot)`

  : Vrne počiščeno različico dane poti.

- `os.path.abspath(pot)`

  : Vrne počiščeno absolutno pot dane poti.

- `os.chdir(pot)`

  : Delovni imenik nastavi na `pot`.

- `os.getcwd()`

  : Vrne trenutni delovni imenik.

**Trenutni imenik** dobimo z `os.getcwd`

```
>>> os.getcwd()
'/Users/matija'
```

Trenutni imenik **nastavimo** z `os.chdir`

```
>>> os.chdir('Documents/uvp')
>>> os.getcwd()
'/Users/matija/Documents/uvp'
>>> os.chdir('..')
>>> os.getcwd()
'/Users/matija/Documents'
>>> os.chdir('uvp')
```

**Imena vseh datotek** v danem imeniku dobimo z `os.listdir`

```
>>> os.listdir()
['datoteke-s-predavanj', 'prosojnice',
'zapiski']
>>> os.chdir('prosojnice')
>>> os.listdir()
['01-uvod-v-python.html', '02-rekurzija.html',
'03-zanke.html', '04-seznami.html',
'05-metode.html', '06-slovarji.html',
'07-iteracija.html', '08-datoteke.html',
'pomozne-datoteke', 'slike', 'staro']
```

Ime **po končnici razdelimo** z `os.path.splitext`

```
>>> os.path.splitext('/imenik/test.txt')
('/imenik/test', '.txt')
```

Ime **po imeniku razdelimo** z `os.path.split`

```
>>> os.path.split('/imenik/test.txt')
('/imenik', 'test.txt')
```

## Pogosti zapisi datotek

**CSV**

Eden najpogostejših zapisov je **JSON**

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

**JSON niz iz Pythonove vrednosti** dobimo s funkcijo `json.dumps`

```
>>> json.dumps([1, {3: True, 4: None}])
'[1, {"3": true, "4": null}]'
```

**Pythonovo vrednost iz JSON niza** dobimo s funkcijo `json.loads`

```
>>> json.loads('[1, {"3": true, "4": null}]')
[1, {'3': True, '4': None}]
```

**JSON datoteko iz Pythonove vrednosti** dobimo s funkcijo `json.dump`

```
with open('primer.json', 'w') as datoteka:
    json.dump(vrednost, datoteka)
```

**Pythonovo vrednost iz JSON datoteke** dobimo s funkcijo `json.load`

```
with open('primer.json') as datoteka:
    vrednost = json.load(datoteka)
```
