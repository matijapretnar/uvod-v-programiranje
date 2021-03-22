---
jupytext:
  cell_metadata_filter: '-all'
  formats: 'md:myst'
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

# Slovarji & množice

Ena najbolj uporabnih podatkovnih struktur v Pythonu so slovarji. Ti so tako kot seznami zbirka vrednosti, le da niso urejeni po zaporedoma oštevilčenih indeksih, temveč vsaka pripada _ključu_. Slovarje pišemo med zavite oklepaje, sestavljeni pa so iz parov `kljuc: vrednost`, ločenih z vejicami. Na primer: `{'a': 1, 'b': 5, 'c': 10}` ali `{1: 'a', 5: 'b', 10: 'c'}`. Ključi se ne smejo ponavljati, lahko pa različnim ključem pripada enaka vrednost. Vrednosti v slovarjih so poljubne, ključi pa so omejeni na nespremenljive vrednosti (na primer lahko so števila, nizi ali nabori, ne pa seznami). Kot smo že omenili, so slovarji zelo uporabni, zato začnimo z nekaj primeri uporabe.

Najočitnejša uporaba slovarjev so slovarji, ki besedam v enem jeziku priredijo njihove prevode:

```python
slo_ang = {
  'abak': 'abacus',
  'abalienacija': 'abalienation',
  'abderit': 'abderite',
  ...
  'žvrkljati': 'whisk'
}
```

Seveda ni nujno, da nizem priredimo nize. Telefonski imenik je primer slovarja, ki nizem priredi številke:

```python
nujne_telefonske_stevilke = {
  'center za obveščanje': 112,
  'policija': 113,
  'informacije': 1188,
  'točen čas': 195
}
```

Lahko pa tudi številkam priredimo nize:

```python
rimske_stevilke = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV',
    5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII',
    9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 100: 'C', 500: 'D',
    1000: 'M'
}
```

Slovarji se pogosto uporabljajo za predstavitev verjetnostih porazdelitev. Ključi so dogodki, pripadajoče vrednosti pa njihove verjetnosti:

```python
met_kocke = {
    1: 1/6, 2: 1/6, 3: 1/6,
    4: 1/6, 5: 1/6, 6: 1/6
}

met_dveh_kock = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36,
    6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36,
    10: 3/36, 11: 2/36, 12: 1/36
}
```

Predstavljamo pa lahko tudi bolj zapletene strukture. Na primer, oglejmo si sledečo matriko:

```python
matrika = [
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [5, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
```

Vidimo, da je razen na nekaj mestih povsod enaka `1`. Takim matrikam pravimo _redke_ in v računalništvu se pogosto pojavljajo. Veliko bolj učinkovito jih predstavimo z njihovo dimenzijo, najpogostejšim elementom ter izjemami. Ker gre za različne vrste podatkov jih bomo predstavili z naborom `(st_vrstic, st_stolpcev, element, izjeme)`, izjeme pa bomo predstavili s slovarjem, kjer bodo ključi mesta `(stolpec, vrstica)` v matriki, vrednosti pa elementi na teh mestih. Na primer, zgornjo matriko bi lahko na bolj učinkovit način predstavili kot:

```python
redka_matrika = (6, 10, 1, {
    (0, 2): 4,
    (1, 0): 5,
    (1, 1): 2,
    (2, 4): 3,
    (4, 2): 4
})
```

Tudi omrežja lahko predstavimo s slovarji. Ključi so vozlišča, vrednosti pa povezave iz teh vozlišč, torej zopet slovarji, ki imajo za ključe ciljna vozlišča, za vrednosti pa razdalje. Na primer, slovenski avtocestni križ, ki je videti kot

![Avtocestni križ](slike/avtoceste.png)

bi lahko predstavili s sledečim slovarjem:

```python
avtocestni_kriz = {
    'LJ': {'KR': 26, 'CE': 73, 'PO': 51, 'NM': 72},
    'KR': {'LJ': 26, 'JE': 35},
    'JE': {'KR': 35},
    'CE': {'MB': 54, 'LJ': 73},
    'MB': {'CE': 54, 'MS': 60},
    'MS': {'MB': 60},
    'PO': {'LJ': 51, 'KP': 64, 'GO': 63},
    'GO': {'PO': 63},
    'KP': {'PO': 64},
    'NM': {'LJ': 72}
}
```

## Osnovne operacije na slovarjih

Slovarji podpirajo precej že poznanih osnovnih operacij. Z `len` dobimo velikost slovarja, torej število parov:

```{code-cell}
len({'a': 6, 'b': 2, 'c': 3})
```

Pozorni moramo biti, da operacije v osnovi delujejo na ključih slovarja:

```{code-cell}
max({1: 10, 2: 20, 3: 30})
```

```{code-cell}
3 in {1: 3, 2: 3, 4: 3}
```

Do posameznih vrednosti dostopamo tako kot pri seznamih, le da namesto indeksa podamo ključ (zaradi česar rezine ne pridejo v poštev):

```{code-cell}
s = {'a': 6, 'b': 2, 'c': 3}
```

```{code-cell}
s['b']
```

Če ključa v slovarju ni, dobimo napako:

```{code-cell}
:tags: ["raises-exception"]
s['d']
```

Tako kot sezname, lahko tudi slovarje spreminjamo:

```{code-cell}
slovar = {'a': 10, 'b': 20}
```

```{code-cell}
slovar['a'] = 50
```

```{code-cell}
slovar
```

V slovarje nove elemente dodajamo tako, da jih priredimo ustreznemu ključu:

```{code-cell}
slovar['c'] = 100
```

```{code-cell}
slovar
```

Elemente lahko pobrišemo z ukazom `del`:

```{code-cell}
del slovar['a']
```

```{code-cell}
slovar
```

## Vgrajene metode na slovarjih

Seveda tudi na slovarjih obstaja kup uporabnih metod, ki so vse naštete v [uradni dokumentaciji](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). Ena najuporabnejših je `get`, ki poskuša dobiti ključu pripadajočo vrednost, vendar ne javi napake, kadar ključa v slovarju ni, temveč vrne `None`.

```{code-cell}
slovar = {'a': 6, 'b': 2, 'c': 3}
```

```{code-cell}
slovar.get('a')
```

```{code-cell}
slovar.get('d')
```

Če želimo, lahko podamo še neobvezni argument, ki pove privzeto vrednost, ki naj se vrne, če ključa ni v slovarju:

```{code-cell}
slovar.get('d', 0)
```

Recimo, da želimo prešteti pojavitve znakov v nizu. Imejmo slovar, ki znakom priredi število njihovih pojavitev ter naredimo sprehod po nizu. Na sprehodu za vsak znak, ki ga srečamo, število pojavitev ustrezno povečamo:

```{code-cell}
def prestej_pojavitve(niz):
    pojavitve = {}
    for znak in niz:
        if znak in pojavitve:
            pojavitve[znak] += 1
        else:
            pojavitve[znak] = 1
    return pojavitve
```

```{code-cell}
prestej_pojavitve('abrakadabra')
```

Če želimo, lahko namesto pogojnega stavka uporabimo tudi metodo `get`:

```{code-cell}
def prestej_pojavitve(niz):
    pojavitve = {}
    for znak in niz:
        pojavitve[znak] = pojavitve.get(znak, 0) + 1
    return pojavitve
```

```{code-cell}
prestej_pojavitve('abrakadabra')
```

Tako kot pri seznamih imamo na voljo `pop`, ki pa ji moramo podati ključ, ki ga želimo odstraniti iz slovarja (saj slovar ni urejen po vrsti, zato nima zadnjega elementa). Metoda ključ odstrani, pripadajočo vrednost pa vrne:

```{code-cell}
slovar = {'a': 10, 'b': 20}
```

```{code-cell}
slovar.pop('a')
```

```{code-cell}
slovar
```

Če res ne vemo, kateri ključ bi odstranili, lahko z metodo `popitem` odstranimo naključni par:

```{code-cell}
slovar = {'a': 10, 'b': 20}
```

```{code-cell}
slovar.popitem()
```

```{code-cell}
slovar.popitem()
```

```{code-cell}
slovar
```

## Zanke na slovarjih

Tudi na slovarjih obstaja zanka `for`, ki pa se sprehaja po _ključih_ slovarja.

```{code-cell}
for x in {'a': 1, 'b': 2, 'c': 3}:
    print(x)
```

V novejših različicah Pythona zanka vrača ključe v takem vrstnem redu, kot smo jih dodajali v slovar, v starejših različicah pa naključno, zato bodite previdni, preden se zanašate na vrstni red.

Če želite dostopati do vrednosti slovarja, uporabite metodo `values`:

```{code-cell}
for x in {'a': 1, 'b': 2, 'c': 3}.values():
    print(x)
```

Z metodo `items` pa lahko dostopate tudi do obojega hkrati:

```{code-cell}
for x in {'a': 1, 'b': 2, 'c': 3}.items():
    print(x)
```

Tako kot smo navajeni od funkcij `enumerate` in `zip`, lahko pare sproti razstavljamo:

```{code-cell}
for k, v in {'a': 1, 'b': 2, 'c': 3}.items():
    print(k, '->', v)
```

Za vajo napišimo program, ki izračuna največjo vrednost v slovarju ter njen pripadajoči ključ. Ideja je podobna kot pri seznamih: po vrsti gledamo vse pare ključev in vrednosti v slovarju. Vsakič, ko vidimo še večjo vrednost, si zapomnimo njen ključ. Ker slovarji niso urejeni po vrsti, ne moremo začeti s prvim elementom, lahko pa si pomagamo z metodo `popitem`.

```{code-cell}
def najvecja_vrednost(s):
    max_k, max_v = s.popitem()
    for k, v in s.items():
        if v > max_v:
            max_k, max_v = k, v
    return max_k, max_v
```

```{code-cell}
najvecja_vrednost(s)
```

Funkcija ima pomanjkljivost, da pokvari vhodni seznam. Jo znate napisati tako, da ga pusti pri miru?

Tako kot sezname, lahko tudi slovarje na eleganten način sestavljamo z izpeljanimi slovarji. Na primer, namesto

```{code-cell}
potence_dve = {}
for i in range(10):
    potence_dve[i] = 2 ** i
potence_dve
```

lahko pišemo tudi:

```{code-cell}
{i: 2 ** i for i in range(10)}
```

Izpeljane slovarje lahko tudi gnezdimo in omejimo s pogoji.

## Množice

S slovarji so v Pythonu tesno povezane tudi _množice_. Vrednosti v množicah pišemo med zavitimi oklepaji ter ločimo z vejicami, na primer `{1, 5, 10}`. Edina izjema je prazna množica, ki jo pišemo kot `set()`, saj `{}` predstavlja že prazen slovar.

Množice uporabljamo, kadar želimo (tako kot pri seznamih) delati s homogeno zbirko podatkov, le da nas ne zanima število ponovitev ter vrstni red. Ker se vsak element v njih pojavi enkrat, vrstni red pa je poljuben, so množice v resnici slovarji, pri katerih gledamo le na ključe, na pripadajoče vrednosti pa ne. Na tak način so množice tudi implementirane.

```{code-cell}
[1, 2, 3] == [2, 1, 3]
```

```{code-cell}
{1, 2, 3} == {2, 1, 3}
```

```{code-cell}
[1, 2, 3] == [1, 1, 2, 3]
```

```{code-cell}
{1, 2, 3} == {1, 1, 2, 3}
```

Na množicah so osnovne operacije unija, presek in razlika, ki jih pišemo kot:

```{code-cell}
{1, 2, 3, 4} | {3, 4, 5, 6}
```

```{code-cell}
{1, 2, 3, 4} & {3, 4, 5, 6}
```

```{code-cell}
{1, 2, 3, 4} - {3, 4, 5, 6}
```

Seveda množice ne bi bile množice, če ne bi mogli preverjati vsebovanosti elementov:

```{code-cell}
1 in {1, 2, 3, 4}
```

```{code-cell}
2 in set()
```

Funkcija `len` nam vrne velikost množice:

```{code-cell}
len({1, 2, 3, 2, 1, 2, 3, 2, 1})
```

Zanka `for` se predvidljivo sprehaja po vseh elementih množice. Vrstni red, v katerem se sprehajamo, pa je malo manj predvidljiv:

```{code-cell}
for x in {'a', 'b', 'c'}:
    print(x)
```

Množice lahko tudi spreminjamo. Elemente dodajamo z metodo `add`, ki deluje podobno kot `append` na seznamih:

```{code-cell}
mn = {1, 2, 3}
```

```{code-cell}
mn.add(4)
mn
```

Na primer, direktno sliko funkcije `f` na množici bi lahko definirali kot:

```{code-cell}
def direktna_slika(f, a):
    slika = set()
    for x in a:
        slika.add(f(x))
    return slika
```

```{code-cell}
direktna_slika(abs, {1, -3, 2, -5, 10})
```

Enako bi lahko dosegli tudi z izpeljano množico:

```{code-cell}
def direktna_slika(f, a):
    return {f(x) for x in a}
```

Elemente odstranjujemo z metodama `remove` in `discard`. Razlika med njima je, da prva javi napako, če elementa ni v množici.

```{code-cell}
mn = {10, 20, 30, 40}
```

```{code-cell}
mn.remove(20)
mn
```

```{code-cell}
:tags: ["raises-exception"]
mn.remove(50)
```

```{code-cell}
mn = {10, 20, 30, 40}
```

```{code-cell}
mn.discard(20)
mn
```

```{code-cell}
mn.discard(50)
mn
```

Metoda `pop` odstrani in vrne naključni element množice:

```{code-cell}
mn = {10, 20, 30}
```

```{code-cell}
mn.pop()
```

```{code-cell}
mn
```

```{code-cell}
mn.pop()
```

```{code-cell}
mn
```

Če želimo dodati več elementov, lahko uporabimo metodo `update`, ki deluje tako, kot `extend` na seznamih.

```{code-cell}
mn = {10, 20, 30}
```

```{code-cell}
mn.update([40, 50])
mn
```

Množico lahko spreminjamo tudi z operacijami `|=`, `&=` in `-=`, ki obstoječo množico povozijo z unijo, presekom in razliko.

```{code-cell}
mn = {10, 20, 30}
```

```{code-cell}
mn |= {40, 50}
mn
```

```{code-cell}
mn = {10, 20, 30, 40}
```

```{code-cell}
mn &= {30, 40, 50}
mn
```

```{code-cell}
mn = {10, 20, 30, 40}
```

```{code-cell}
mn -= {30, 40, 50}
mn
```

Tako kot pri spreminjanju seznamov, je treba biti previden tudi pri spreminjanju množic (no, in tudi slovarjev). Na primer, ali spodnja programa delujeta enako?

```{code-cell}
mn = mn & {10, 20, 30, 40}
```

```{code-cell}
mn &= {10, 20, 30, 40}
```

Videti je, da je drugi le okrajšava za prvega, vendar ni res. Prvi izračuna presek ter dobljeno množico shrani pod imenom `mn`. Drugi ukaz pa spremeni množico, na katero kaže `mn`. Razliko lahko vidimo, če se na isto množico skličemo še pod drugim imenom:

```{code-cell}
mn = {1, 2, 5, 10, 20, 25}
```

```{code-cell}
mn2 = mn
```

```{code-cell}
mn = mn & {10, 20, 30, 40}
```

```{code-cell}
mn
```

```{code-cell}
mn2
```

Tako `mn` kot `mn2` sta na začetku kazala na množico s šestimi elementi. Nato smo izračunali presek ter ga shranili pod ime `mn`, vendar je `mn2` še vedno kazal na isto množico. Sedaj pa isto ponovimo še z `&=`:

```{code-cell}
mn = {1, 2, 5, 10, 20, 25}
```

```{code-cell}
mn2 = mn
```

```{code-cell}
mn &= {10, 20, 30, 40}
```

```{code-cell}
mn
```

```{code-cell}
mn2
```

Ukaz `&=` je spremenil množico, na katero je kazalo ime `mn`. Ker je na isto množico na začetku kazalo tudi ime `mn2`, zadnji klic pokaže presek.
