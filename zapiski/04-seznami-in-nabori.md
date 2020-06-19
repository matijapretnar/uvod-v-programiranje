# Seznami & nabori

Če želimo delati z zaporedjem podatkov, uporabimo sezname.

```python
[1, 2, 3]    ['a', 'b']    []

[[True], [False], [True, False]]
```

Sename pišemo v oglatih oklepajih, med katerimi napišemo vrednosti, ločene z vejicami, na primer `[10, 20, 30]` je seznam, ki vsebuje tri števila, `[]` pa prazen seznam. Če želimo, lahko vejico pišemo tudi za zadnjim elementom. Seznami so lahko tudi gnezdeni. Na primer, matriko bi predstavili s seznamom seznamov:

```
[[1, 2, 3],

:   [4, 5, 6], [7, 8, 9]]
```

V sezname lahko spravimo vrednosti različnih tipov, na primer:

```
[1, True, [2, 5], "Niz", 3.14]
```

Vendar običajno sezname uporabimo za predstavitev homogene zbirke podatkov, torej da so vse vrednosti istega tipa.

## Vgrajene metode na seznamih

Osnovne operacije na seznamih

```python
>>> prastevila = [2, 3, 5, 7, 11, 13, 17]
>>> prazen_seznam = []
>>> [True, False] + [True]
[True, False, True]
>>> 3 * ['x', 'y']
['x', 'y', 'x', 'y', 'x', 'y']
>>> 5 in prastevila
True
>>> [5, 7, 11] in prastevila
False
>>> sum([1, 2, 3, 4, 5])
15
```

Tako kot nize lahko tudi sezname stikamo z operacijo `+` in množimo s celimi števili:

```
>>> [10, 20, 30] + [6, 5, 4] [10, 20, 30, 6, 5, 4]
>>> 4 *
[1, 2] [1, 2, 1, 2, 1, 2, 1, 2]
```

Dolžino seznama dobimo s funkcijo `len`:

```
>>> len([100, 200, 300]) 3
>>> len([]) 0
```

Tudi na seznamih imamo na voljo predikata `in` in `not in`, s katerima ugotovimo, ali se nek element pojavlja v seznamu:

```
>>> 'Ema' in ['Ana', 'Bojan', 'Cvetka', 'David'] False
>>> 'Ana' in ['Ana', 'Bojan', 'Cvetka', 'David'] True
```

```
def stevilo_dni(mesec, leto):

:   

    if mesec == 2:

    :   return 29 if je_prestopno(leto) else 28

    elif mesec in [1, 3, 5, 7, 8, 10, 12]:

    :   return 31

    elif mesec in [4, 6, 9, 11]:

    :   return 30
```

```
>>> povprecje([1, 2, 3])
2.0
>>> povprecje([])
>>> povprecje([1, 2, 4, 8, 16])
6.2
```

```
>>> razpon([1, 2, 3])
2
>>> razpon([])
>>> razpon([1, 2, 4, 8, 16])
15
```

Indeksiranje in rezine na seznamih delujejo tako kot na nizih:

```
>>> sez = [5, 3, 8, 2, 5, 2, 1, 2]
>>> sez[0] 5
>>>
sez[2] 8
>>> sez[len(sez) - 1] 2
>>> sez[-1] 2
>>>
sez[:2] [5, 3]
>>> sez[1:3] [3, 8]
>>> sez[3:] [2, 5,
2, 1, 2]
>>> sez[1:5:2] [3, 2]
>>> sez[::2] [5, 8, 5, 1]
```

Če imamo gnezdene sezname, do elementov dostopamo z gnezdenimi indeksi:

>

> > > mat = [[1, 0, 0], [0, -1, 2], [3, 1, 5]] mat[0][0] 1 mat[1][-1] 2

Na primer, sled matrike bi lahko izračunali kot:

```
def sled(matrika):

:   '''Izračuna sled dane matrike.''' vsota_diagonalnih = 0 for i
    in range(len(matrika)): vsota_diagonalnih += matrika[i][i]
    return vsota_diagonalnih
```

```
>>> mat = [[5]]
>>> sled(mat) 5
```

Sledi pa nikakor ne bomo izračunali na sledeči (pri študentih dostikrat videni) način:

```
def grozna_sled(matrika):

:   '''Na popolnoma napačen izračuna sled dane matrike.'''
    vsota_diagonalnih = 0 for i in range(len(matrika)): for j in
    range(len(matrika)): if i == j: vsota_diagonalnih +=
    matrika[i][j] return vsota_diagonalnih
```

Funkcija sled matrike sicer izračuna pravilno, vendar na izjemno potraten način, saj se sprehodi čez celotno matriko, ne le čez diagonalne elemente. Na primer, pri matriki velikosti $1000 \times 1000$ bi druga funkcija pregledala tisočkrat več elementov (in posledično porabila tisočkrat več časa).

```python
>>> prastevila = [2, 3, 5, 7, 11, 13, 17]
>>> prastevila[2]
5
>>> prastevila[-2]
13
>>> prastevila[2:-2]
[5, 7, 11]
>>> prastevila[::2]
[2, 5, 11, 17]
```

```
>>> vsota_elementov([-5, 2, 10, -13, 0])
-6
>>> vsota_elementov([])
0
```

```
>>> stevilo_elementov([-5, 2, 10, -13, 0])
5
>>> stevilo_elementov([])
0
```

```
>>> vsebuje_sodega([-5, 2, 10, -13, 0])
True
>>> vsebuje_sodega([])
False
>>> vsebuje_sodega([1, 3, 5])
False
```

Sezname lahko tudi **gnezdimo**

```python
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> m[1]
[4, 5, 6]
>>> m[1][2]
6
```

Z zanko `for` se lahko vozimo **po seznamih**:

```
for x in [10, 20, 30]:
    print(x)
```

```
10
20
30
```

Tako kot se lahko z zanko `for` sprehodimo po vseh znakih v nizu, se lahko z njo sprehodimo tudi po vseh elementih danega seznama:

```
def vsota_elementov(seznam):

:   '''Vrne vsoto elementov v danem seznamu.''' vsota = 0 for
    trenutni in seznam: vsota += trenutni return vsota
```

```
>>> vsota_elementov([10, 2, 4000, 300]) 4312
```

Največji element v danem seznamu lahko poiščemo tako, da zaporedoma vsak element seznama primerjamo z do sedaj največjim videnim elementom. Če je trenutni element večji, do sedaj največji element popravimo. Ko pregledamo vse elemente v seznamu, je do sedaj največji element tudi na splošno največji element. Edina stvar, na katero moramo še paziti, je ta, da na začetku izberemo ustrezen največji element. Tu imamo dve dobri izbiri. (Slaba izbira bi bila, da bi za največji do zdaj viden element vzeli neko dovolj majhno število, na primer 0 ali -9999999 -- ta izbira je očitno napačna!) Prva dobra izbira je kar prvi element v seznamu, pri čemer moramo potem poprej preveriti še to, da je seznam neprazen:

```
def najvecji_element(seznam):

:   '''Vrne največji element v danem seznamu. Če ga ni, vrne
    None''' if len(seznam) == 0: return najvecji_do_zdaj =
    seznam[0] for trenutni in seznam: if trenutni >
    najvecji_do_zdaj: najvecji_do_zdaj = trenutni return
    najvecji_do_zdaj
```

Druga izbira pa je `None`, vendar moramo potem pri vsaki primerjavi pogledati, ali imamo že "pravi" največji element ali je to do sedaj še vedno `None`:

```
def najvecji_element(seznam):

:   '''Vrne največji element v danem seznamu. Če ga ni, vrne
    None''' najvecji_do_zdaj = None for trenutni in seznam: if
    najvecji_do_zdaj == None or trenutni > najvecji_do_zdaj:
    najvecji_do_zdaj = trenutni return najvecji_do_zdaj
```

```
>>> najvecji_element([10, 2, 4000, 300]) 4000
```

Seveda lahko uporabimo tudi vgrajene funkcije:

```
>>> sum([10, 2, 4000, 300]) 4312
>>> min([10, 2, 4000, 300]) 2
>>> max([10, 2, 4000, 300]) 4000
```

```
>>> vsota_elementov([-5, 2, 10, -13, 0])
-6
>>> vsota_elementov([])
0
```

```
>>> stevilo_elementov([-5, 2, 10, -13, 0])
5
>>> stevilo_elementov([])
0
```

```
>>> vsebuje_sodega([-5, 2, 10, -13, 0])
True
>>> vsebuje_sodega([])
False
>>> vsebuje_sodega([1, 3, 5])
False
```

## Spreminjanje seznamov

Za razliko od nizov lahko vrednosti v seznamih tudi spreminjamo:

```
>>> sez = [10, 20, 30]
>>> sez[1]
20
>>> sez[1] = 40
>>> sez
[10, 40, 30]
```

Zamenjamo lahko tudi celotno **rezino**

```
>>> sez = [10, 20, 30, 40]
>>> sez[1:3]
[20, 30]
>>> sez[1:3] = [0, 0, 0]
>>> sez
[10, 0, 0, 0, 40]
```

Če nadomestna rezina ni enake dolžine kot prvotna, se seznam ustrezno skrajša ali podaljša

Kot vidimo, lahko nadomestimo tudi prazno rezino, s čimer nove elemente vrinemo v seznam. Nadomeščanje prazne rezine ni isto kot nadomeščanje elementa z istim indeksom kot rezina:

Elemente lahko tudi **brišemo**

```
>>> sez = [10, 20, 30]
>>> sez[1]
20
>>> del sez[1]
>>> sez
[10, 30]
```

Tudi rezine lahko brišemo:

```
>>> del sez[1:4]
>>> sez [5, 0, 1, 500]
```

Seznami so **spremenljive strukture**

```
>>> x = [1, 1, 1]
>>> y = x
>>> x = [2, 2, 2]
>>> y
[1, 1, 1]
```

```
>>> x = [1, 1, 1]
>>> y = x
>>> x[2] = 2
>>> y
[1, 1, 2]
```

Da je zmeda večja, `+=` **ni isto** kot `=` & `+`

```
>>> x = [1, 1, 1]
>>> y = x
>>> x += [2, 2, 2]
>>> y
[1, 1, 1, 2, 2, 2]
```

```
>>> x = [1, 1, 1]
>>> y = x
>>> x = x + [2, 2, 2]
>>> y
[1, 1, 1]
```

Pri spreminjanju seznamov je treba biti previden, saj ne deluje tako, kot smo navajeni pri spreminjanju vrednosti spremenljivk. Na primer, pišimo

```
>>> a = 5
>>> b = a
>>> a = 0
>>> b 5
```

Vidimo, da se vrednost spremenljivke `b` ni spremenila, saj smo jo v drugi vrstici nastavili na število 5\. Pri seznamih je stvar malo drugačna. Če pišemo

```
>>> a = [1, 2, 3]
>>> b = a
>>> a = []
>>> b [1, 2, 3]
```

so stvari še vedno take, kot bi jih pričakovali. Vrednost `b` smo nastavili na isti seznam kot `a`, vendar smo potem rekli, da naj bo v `a` shranjen drugačen seznam, s čimer na vrednost v `b` nismo vplivali. Če pa pišemo

```
>>> a = [1, 2, 3]
>>> b = a
>>> a[1] = 20
>>> b [1, 20,
3]
```

se je s tem, ko smo spremenili `a`, spremenil tudi `b`. Kaj se je zgodilo? Ko smo napisali `b = a`, smo povedali, naj bo v `b` shranjen isti seznam kot `a`. In z `a[1] = 20` smo povedali, naj se na mesto `1` v seznamu, shranjenem v `a`, zapiše 20\. Ker je v `b` shranjen isti (ne le enak) seznam kot v `a`, je s tem tudi seznam v `b` drugačen.

Pogosta past, v katero se na začetku ujamemo zaradi spremenljivosti seznamov, je izračun identične matrike. Vemo že, da lahko v Pythonu seznam pomnožimo s številom:

```
>>> 3 * [0] [0, 0, 0]
```

To nam da idejo, da bi lahko na isti način izračunali ničelno matriko:

```
>>> 3 * [3 * [0]] [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

Izračun je videti pravilen, vendar vse tri vrstice te matrike kažejo na isti seznam. To je tako, kot če bi pisali:

```
>>> vrstica = [0, 0, 0]
>>> matrika = [vrstica, vrstica,
vrstica]
```

Poskusimo iz te matrike dobiti identično matriko tako, da po diagonali nastavimo enice. Najprej nastavimo prvi element v prvi vrstici:

```
>>> matrika[0][0] = 1
>>> matrika [[1, 0, 0], [1, 0, 0],
[1, 0, 0]]
```

Kaj se je zgodilo? Ker druga in tretja vrstica kažeta na isti seznam kot prva, smo tudi v njima prvi element popravili na 1\. Če sedaj nastavimo še drugi element v drugi vrstici in tretjega v tretji vrstici se zgodba ponovi:

```
>>> matrika[1][1] = 1
>>> matrika[2][2] = 1
>>> matrika
[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
```

Če želimo identično matriko izračunati na pravilen način, moramo za predstavitev vsake vrstice podati svoj seznam, zato ne moremo uporabiti le pomnoževanja seznamov.

## Metode na seznamih

Za večino pogosto uporabljanih stvari na seznamih obstajajo že vgrajene metode. Te povečini ne vračajo ničesar, temveč le spremenijo dani seznam. Izjemi sta metodi `index` in `count`, ki vrneta vrednost in seznam pustita pri miru, ter metoda `pop` ki tako spremeni seznam kot vrne vrednost.

- `sez.append(x)`

  : Dodaj element [x]{.title-ref} na konec seznama `sez`.

- `sez.extend(sez2)`

  : Na konec seznama `sez` dodaj vse elemente iz seznama `sez2`.

- `sez.insert(i, x)`

  : Pred element na mestu `i` v seznamu `sez` vstavi element `x`.

- `sez.remove(x)`

  : Iz seznama `sez` odstrani prvo pojavitev vrednosti `x`.

- `sez.pop(i=-1)`

  : Vrni element na mestu `i` v seznamu `sez` in odstrani ta element

  ```
  iz seznama. Če indeksa `i` ne podamo, metoda odstrani zadnji
  element.
  ```

- `sez.clear()`

  : Iz seznama `sez` pobriši vse elemente.

- `sez.index(x)`

  : Vrni prvo mesto, na katerem se v seznamu `sez` nahaja vrednost

  ```
  `x`.
  ```

- `sez.count(x)`

  : Vrni število pojavitev vrednosti `x` v seznamu `sez`.

- `sez.sort(key=None, reverse=False)`

  : Na mestu uredi seznam glede na vrednosti funkcije `key`. Če

  ```
  parameter `reverse` nastavimo na `True`, bo seznam urejen
  padajoče.
  ```

- `sez.reverse()`

  : Obrni seznam `sez` na glavo.

Elemente **na konec dodajamo** z `append`

```python
>>> sez = [10, 20, 30]
>>> sez.append(40)
>>> sez
[10, 20, 30, 40]
```

Metodo `append` pogosto uporabljamo za izračun seznama ustreznih elementov. To storimo tako, da ustvarimo prazen seznam, nato pa vanj z metodo `append` dodamo vsak ustrezen element. To je podoben postopek kot pri izračunu vsote ustreznih elementov, kjer smo ustvarili spremenljivko z začetno vrednostjo 0, nato pa ji prištevali ustrezne elemente.

```python
>>> seznam_kvadratov([1, 6, -3, 0, 4, 2])
[1, 36, 9, 0, 16, 4]

>>> dolzine_besed(['mama', 'je', 'tam'])
[4, 2, 3]

>>> seznam_delnih_vsot([1, 6, -3, 0, 4, 2])
[1, 7, 4, 4, 8, 10]

>>> sodi_elementi([1, 6, -3, 0, 4, 2])
[6, 0, 4, 2]
```

```
def vsota_pozitivnih_elementov(seznam):

:   '''Vrne vsoto vseh pozitivnih elementov danega seznama.'''
    vsota = 0 for element in seznam: if element > 0: vsota += element
    return vsota

def pozitivni_elementi(seznam):

:   '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
    pozitivni = [] for element in seznam: if element > 0:
    pozitivni.append(element) return pozitivni
```

```
>>> vsota_pozitivnih_elementov([1, -5, 2, 3]) 6
>>>
pozitivni_elementi([1, -5, 2, 3]) [1, 2, 3]
```

Zadnji element **snamemo** s `pop`

```python
>>> sez = [10, 20, 30]
>>> sez.pop()
30
>>> sez
[10, 20]
```

Elemente na dano mesto **vstavimo** z `insert`

```python
>>> sez = [10, 20, 30]
>>> sez.insert(1, 0)
>>> sez
[10, 0, 20, 30]
```

**Več elementov** dodamo z `extend`

```python
>>> sez = [10, 20, 30]
>>> sez.extend([40, 50])
>>> sez
[10, 20, 30, 40, 50]
```

### **Okrajšava** za `extend` je `+=`

```python
>>> sez = [10, 20, 30]
>>> sez += [40, 50]
>>> sez
[10, 20, 30, 40, 50]
```

Eno pojavitev elementa **odstranimo** z `remove`

```python
>>> sez = [1, 2, 1, 2, 3]
>>> sez.remove(2)
>>> sez
[1, 1, 2, 3]
```

Seznam **izpraznimo** s `clear`

```python
>>> sez = [1, 2, 1, 2, 3]
>>> sez.clear()
>>> sez
[]
```

Seznam **obrnemo** z `reverse`

```python
>>> sez = [1, 2, 4, 8, 16]
>>> sez.reverse()
>>> sez
[16, 8, 4, 2, 1]
```

### **Obrnjen seznam** dobimo z rezinami

```python
>>> sez = [1, 2, 4, 8, 16]
>>> sez[::-1]
[16, 8, 4, 2, 1]
>>> sez
[1, 2, 4, 8, 16]
```

Seznam **uredimo** z `sort`

```python
>>> sez = [4, 1, 8, 2, 16]
>>> sez.sort()
>>> sez
[1, 2, 4, 8, 16]
```

### **Urejen seznam** dobimo s `sorted`

```python
>>> sez = [4, 1, 8, 2, 16]
>>> sorted(sez)
[1, 2, 4, 8, 16]
>>> sez
[4, 1, 8, 2, 16]
```

## Izpeljani seznami

Python omogoča, da sezname tvorimo na enostaven način z **izpeljanimi seznami**, ki so oblike `[izraz for spremenljivka in mozne_vrednosti]`, podobno kot v matematiki množice pišemo kot ${ 2 \cdot n \mid n \in {1, \dots, 9}}$: .. doctest:

```
>>> [2 * n for n in range(1, 10)]
[2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> potence = [2 ** n for n in range(10)]
>>> potence
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
>>> [n - 1 for n in potence]
[0, 1, 3, 7, 15, 31, 63, 127, 255, 511]
>>> [int(stevka) for stevka in str(3141592)]
[3, 1, 4, 1, 5, 9, 2]
```

Če želimo, lahko v izpeljani seznamih oblike `[izraz for spremenljivka in mozne_vrednosti if pogoj]` s pogojem določimo, katere elemente želimo:

```
>>> [2 * n for n in range(1, 10) if n % 3 == 1] [2, 8, 14]
```

Sezname dostikrat lepše zgradimo z **izpeljanimi seznami**

```
seznam = []
for x in ...:
    seznam.append(f(x))
```

```
seznam = [f(x) for x in ...]
```

Sezname dostikrat lepše zgradimo z **izpeljanimi seznami**

```
def pozitivni_elementi(seznam):

:   '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
    return [element for element in seznam if element > 0]

def vsota_pozitivnih_elementov(seznam):

:   '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
    return sum([element for element in seznam if element > 0]) # ali
    pa kar # return sum(pozitivni_elementi(seznam))
```

```
def seznam_kvadratov(seznam):
    kvadrati = []
    for x in seznam:
        kvadrati.append(x ** 2)
    return kvadrati
```

```
def seznam_kvadratov(seznam):
    return [x ** 2 for x in seznam]
```

```
def seznam_absolutnih_vrednosti(seznam):
    absolutne_vrednosti = []
    for x in seznam:
        absolutne_vrednosti.append(abs(x))
    return absolutne_vrednosti
```

```
def seznam_absolutnih_vrednosti(seznam):
    return [abs(x) for x in seznam]
```

```
def seznam_absolutnih_vrednosti(seznam):
    absolutne_vrednosti = []
    for x in seznam:
        absolutne_vrednosti.append(abs(x))
    return absolutne_vrednosti
```

```
def seznam_absolutnih_vrednosti(seznam):
    return [abs(x) for x in seznam]
```

```
def dolzine_besed(besede):
    dolzine = []
    for beseda in besede:
        dolzine.append(len(beseda))
    return dolzine
```

```
def dolzine_besed(besede):
    return [len(beseda) for beseda in besede]
```

```
def identicna_matrika(n):

:   '''Vrne identično matriko velikosti n x n.''' matrika = [n *
    [0] for _ in range(n)] for k in range(len(matrika)):
    matrika[k][k] = 1 return matrika
```

```
>>> identicna_matrika(3) [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

Izpeljani seznami **niso vedno rešitev**

```
def delne_vsote(seznam):
    vsote = []
    vsota = 0
    for x in seznam:
        vsota += x
        vsote.append(vsota)
    return vsote
```

```
def delne_vsote(seznam):
    return [
        sum(seznam[:i + 1])
        for i in range(len(seznam))
    ]
```

V izpeljanih seznamih imamo lahko tudi **gnezdene zanke**

```
seznam = []
for x in ...:
    for y in ...:
        seznam.append(f(x, y))
```

```
seznam = [f(x, y) for x in ... for y in ...]
```

V izpeljanih seznamih imamo lahko **pogoje**

```
seznam = []
for x in ...:
    if pogoj:
        seznam.append(f(x))
```

```
seznam = [f(x) for x in ... if pogoj]
```

V izpeljanih seznamih imamo lahko **pogoje**

```
def sodi_elementi(seznam):
    sodi = []
    for x in seznam:
        if x % 2 == 0:
            sodi.append(x)
    return sodi
```

```
def sodi_elementi(seznam):
    return [x for x in seznam if x % 2 == 0]
```

## Razlika med `sort` in `sorted`

## Nabori

Nabori se obnašajo podobno kot seznami, le da njihovih vrednosti ne moremo spreminjati. Pišemo jih tako kot sezname, le med običajne oklepaje: `(1, 2, 3)`. Nabor z enim elementom pišemo kot `(1, )` (razmislite, zakaj ga ne pišemo kot `(1)`). Včasih lahko nabore pišemo kar brez oklepajev:

```python
(3, 3, 2020)    ()     (1,)

(46.0422504, 14.4897114)

('Matija', 'Pretnar', 27004498)
```

Druga razlika pa je ta, da so nabori običajno heterogeni: elementi na različnih mestih imajo lahko različne tipe in različne pomene:

Sicer za nabore veljajo podobne lastnosti: lahko jih stikamo in množimo; lahko izračunamo njihovo vsoto, minimum, maksimum in dolžino; s predikatom `in` lahko pogledamo, ali vsebujejo dani element; lahko jih indeksiramo in delamo rezine; po njih se lahko sprehodimo z zanko `for`; od metod pa sta na voljo le `count` in `index`, saj ti dve edini ne spreminjata ničesar.

```python
>>> (True, False) + (True,)
(True, False, True)
>>> 3 * ('x', 'y')
('x', 'y', 'x', 'y', 'x', 'y')
>>> 5 in (1, 2, 3)
False
>>> (1, 2, 5, 10, 20, 50)[3]
10
>>> (1, 2, 5, 10, 20, 50)[3:]
(10, 20, 50)
```

## Razlika med seznami in nabori

**Kdaj uporabimo** sezname, kdaj pa nabore?

### Nabori: fiksna dolžina, različni pomeni

```
>>> datum = (3, 3, 2020)
>>> fmf = (46.0422504, 14.4897114)
>>> jaz = ('Matija', 'Pretnar', 27004498)
```

### Seznami: poljubna dolžina, en pomen

```
>>> leta = [2012, 2016, 2020, 2024]
>>> opravili_bodo_uvp = []
>>> datumi = [(3, 3, 2020), (25, 6, 1991)]
```

Nabori in nizi so **nespremenljive strukture**

```
>>> x = (1, 1, 1)
>>> x[2] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError:
  'tuple' object does not support item assignment
```

```
>>> x = 'abc'
>>> x[2] = 'd'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError:
  'str' object does not support item assignment
```

## Iskanje z bisekcijo

Eden najosnovnejših problemov, ki ga rešujemo z računalniki, je iskanje določenega podatka v veliki zbirki. Pri tem obravnavamo dve varianti:

1. Dano imamo zbirko elementov, nas pa zanima, ali iskani element v njej obstaja. Na primer, zanima nas, ali se beseda _drabostljiv_ pojavi v slovarju slovenskega knjižnega jezika.
2. Dano imamo zbirko ključev in pripadajočih vrednosti, nas pa zanima, ali ima iskani ključ v zbirki pripadajočo vrednost in kakšna je. Na primer, zanima nas ne samo to, ali je beseda _drabostljiv_ v slovarju, temveč tudi to, kakšno je geslo, ki ji pripada.

Za začetek predpostavimo, da je naša zbirka predstavljena z neurejenim seznamom, v katerem so našteti vsi elementi. Na primer:

```
sskj = ['miza', 'vesel', 'žaga', ..., 'razsvetljenstvo']
```

Če je seznam neurejen, obstaja bolj ali manj le en način, s katerim ugotovimo, ali se element v seznamu pojavi: sprehodimo se čez vse elemente seznama od prvega do zadnjega (lahko tudi od zadnjega do prvega) in vsakega primerjamo z iskanim. Če najdemo enakega, je iskani element v seznamu. Če pa preiščemo vse elemente in ne najdemo enakega, iskanega elementa v seznamu ni.

```
def poisci_v_neurejenem(seznam, iskani_element):

:   '''Vrne True, če se iskani element pojavi v seznamu, in False, če
    se ne.''' for element in seznam: if element == iskani_element:
    return True return False
```

```
>>> poisci_v_neurejenem([1, 5, 2, 3], 4) False
>>>
poisci_v_neurejenem([1, 5, 2, 3], 3) True
```

Boljše rešitve od tega, da preiščemo vse elemente, žal ni. Če kakšen algoritem ne bi pregledal vseh elementov, preden bi se odločil, da iskanega elementa ni v seznamu, bi lahko vse elemente, ki si jih je ogledal, zamenjali z iskanim, algoritem pa bi se še vedno odločil, da iskanega elementa v seznamu ni, saj bi v drugo glede na pregledane elemente moral sprejeti iste odločitve kot prvič.

Z neurejenim seznamom parov lahko predstavimo tudi zbirko ključev in pripadajočih vrednosti:

```
sskj = [('miza', 'lesen predmet za odlaganje krožnikov),
        ('vesel', 'tisti, ki izraža veselje'),
        ('žaga', 'orodje za žaganje'), ...,
        ('razsvetljenstvo', 'zgodovinsko obdobje, znano po žarnicah')]
```

Postopek za iskanje je podoben prejšnjemu, le da se tokrat vozimo čez pare in ključe primerjamo z iskanim. Če najdemo ujemajoč ključ, vrnemo pripadajočo vrednost, sicer pa vrnemo `None`.

```
def poisci_vrednost_v_neurejenem(seznam, iskani_kljuc):

:   '''Vrne pripadajočo vrednost ključa v seznamu. Ce je ni, vrne
    None.''' for kljuc, vrednost in seznam: if kljuc ==
    iskani_kljuc: return vrednost return None
```

```
>>> poisci_vrednost_v_neurejenem([(7, 'a'), (4, 'r'), (8,
't')], 7) 'a'
>>> poisci_vrednost_v_neurejenem([(7, 'a'),
(4, 'r'), (8, 't')], 5)
>>>
poisci_vrednost_v_neurejenem([(7, 'a'), (4, 'r'), (8, 't')],
'r')
```

Tudi v zadnjem klicu smo dobili rezultat `None`, saj se `'r'` v seznamu pojavi le kot vrednost, ne kot ključ.

Če je seznam urejen, lahko iskani element poiščemo bistveno hitreje z bisekcijo. V seznamu si pogledamo element na sredini. Če je slučajno enak iskanemu elementu, smo končali, sicer pa je bodisi večji bodisi manjši. Če je sredinski element večji od iskanega, potem vemo, da se iskani element ne more pojaviti v desni polovici, saj so vsi tamkajšnji elementi zaradi urejenosti večji od sredinskega. Tako lahko iskanje zožimo le na levo polovico seznama. Če je sredinski element manjši od iskanega, pa iskanje zožimo na desno polovico seznama. V obeh primerih iskanje nadaljujemo na polovico manjšem seznamu, kjer uporabimo enak postopek. To nadaljujemo dokler iskanja ne zožimo na seznam dolžine 1\. V tem primeru le pogledamo, če je edini element enak iskanemu. Če je, smo iskani element našli, če ni, pa ga v seznamu ni bilo.

Bisekcijo lahko implementiramo na več načinov. Prvi je, da v spremenljivkah `zacetek` in `konec` hranimo začetni in končni indeks podseznama, v katerem iščemo element. V skladu s Pythonovimi standardi, v spremenljivki `konec` ne bomo hranili zadnjega indeksa v podseznamu, temveč naslednji indeks. Na začetku bomo element iskali v celotnem seznamu, zato bo `zacetek` enak 0, `konec` pa dolžini seznama. Odvisno od tega, kakšen je sredinski element v primerjavi z iskanim, bomo spremenljivki `zacetek` in `konec` ustrezno popravljali. Ko se indeksa izenačita, postopek končamo, saj je tedaj podseznam prazen.

```
def poisci_v_urejenem_z_zanko(seznam, iskani_element):

:   '''Vrne True, če se iskani element pojavi v urejenem seznamu, in
    False, če se ne.''' zacetek = 0 konec = len(seznam)

    while zacetek < konec:

    :   sredina = (zacetek + konec) // 2 if seznam[sredina] ==
        iskani_element: return True elif seznam[sredina] <
        iskani_element: zacetek = sredina + 1 elif seznam[sredina] >
        iskani_element: konec = sredina

    return False
```

```
>>> poisci_v_urejenem_z_zanko([1, 2, 3, 5], 4) False
>>>
poisci_v_urejenem_z_zanko([1, 2, 3, 5], 3) True
```

Seveda funkcija ne bo delala pravilno, če ji ne bomo podali urejenega seznama:

```
>>> poisci_v_urejenem_z_zanko([3, 3, 3, 1, 5, 5, 5], 3) False
```

Enak postopek zapišemo tudi rekurzivno, vendar moramo biti pri tem malo bolj previdni. Načeloma lahko iskanje v podseznamu naredimo tako, da s pomočjo rezin ustvarili manjši seznam in iščemo v njem:

```
def poisci_v_urejenem_z_rezinami(seznam, iskani_element):

:   '''Vrne True, če se iskani element pojavi v urejenem seznamu, in
    False, če se ne.''' if len(seznam) == 0: return False else:
    sredina = len(seznam) // 2 if seznam[sredina] == iskani_element:
    return True elif seznam[sredina] < iskani_element: return
    poisci_v_urejenem_z_rezinami(seznam[sredina + 1:],
    iskani_element) elif seznam[sredina] > iskani_element: return
    poisci_v_urejenem_z_rezinami(seznam[:sredina],
    iskani_element)
```

```
>>> poisci_v_urejenem_z_rezinami([1, 2, 3, 5], 4) False
>>>
poisci_v_urejenem_z_rezinami([1, 2, 3, 5], 3) True
```

Taka funkcija sicer deluje pravilno, vendar opravlja nepotrebno delo, saj ob vsakem rekurzivnem klicu naredi novo rezino (bodisi `seznam[sredina + 1:]` bodisi `seznam[:sredina]`), kar zahteva, da vse ustrezne elemente presname na novo mesto. Bolje je, da tako kot pri rešitvi z zankami ves čas delamo z istim seznamom, vendar si zapomnimo, med katerima dvema indeksoma iščemo element.

```
def poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek, konec):

:   '''Vrne True, če se iskani element pojavi v urejenem seznamu na
    mestu i, kjer je zacetek <= i < konec, in False, če se ne.'''
    if zacetek == konec: return False else: sredina = (zacetek + konec)
    // 2 if seznam[sredina] == iskani_element: return True elif
    seznam[sredina] < iskani_element: return
    poisci_v_urejenem_med_indeksoma(seznam, iskani_element,
    sredina + 1, konec) elif seznam[sredina] > iskani_element:
    return poisci_v_urejenem_med_indeksoma(seznam, iskani_element,
    zacetek, sredina)
```

```
>>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 4, 0, 3)
False
>>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0,
3) True
>>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0,
2) False
```

Ta rešitev je veliko bolj učinkovita, saj ne ustvarja novih elementov, je pa malo moteče, ker moramo vsakič podajati meje. Če tega ne želimo, lahko uporabimo bodisi pomožno funkcijo:

```
def poisci_v_urejenem(seznam, iskani_element):

:   '''Vrne True, če se iskani element pojavi v urejenem seznamu, in
    False, če se ne.''' return
    poisci_v_urejenem_med_indeksoma(seznam, iskani_element, 0,
    len(seznam))
```

bodisi argumentoma `zacetek` in `konec` damo privzeti vrednosti:

```
def poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek=0, konec=None):

:   '''Vrne True, če se iskani element pojavi v urejenem seznamu na
    mestu i, kjer je zacetek <= i < konec, in False, če se ne.'''
    if konec is None: konec = len(seznam)

    if zacetek == konec:

    :   return False

    else:

    :   sredina = (zacetek + konec) // 2 if seznam[sredina] ==
        iskani_element: return True elif seznam[sredina] <
        iskani_element: return
        poisci_v_urejenem_med_indeksoma(seznam, iskani_element,
        sredina + 1, konec) elif seznam[sredina] > iskani_element:
        return poisci_v_urejenem_med_indeksoma(seznam,
        iskani_element, zacetek, sredina)
```

```
>>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 3) True
>>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3) True
>>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 2)
False
```

Kot vidimo, smo privzeto vrednost argumenta `zacetek` nastavili na 0, privzete vrednosti argumenta `konec` pa nismo nastavili na dolžino seznama. Razlog je v tem, da vrednost privzetega argumenta lahko nastavimo le enkrat: takrat, ko funkcijo definiramo. Ker pa hočemo funkcijo uporabiti na seznamih različnih dolžin, nobena privzeta vrednost ne bo prava. Običajna rešitev je, da argumentom, za katere lahko privzete vrednosti izračunamo šele ob klicu funkcije, nastavimo privzeto vrednost `None`. Nato pa ob klicu funkcije v primerih, ko se je uporabila ta privzeta vrednost, vrednost argumenta ustrezno popravimo. V našem primeru smo takrat, ko je bila vrednost spremenljivke `konec` enaka `None`, njeno vrednost nastavili na dolžino danega seznama. V primeru, ko smo ob klicu funkcije vrednost argumenta `konec` podali (torej ob rekurzivnih klicih), pa bo ta vrednost različna od `None`, zato se ne bo zgodilo nič.
