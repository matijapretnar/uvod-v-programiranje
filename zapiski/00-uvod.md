---
jupytext:
  cell_metadata_filter: '-all'
  formats: 'md:myst'
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Uvod v programiranje

Programiranje različnim ljudem [pomeni](https://sl.wikipedia.org/wiki/Nevrolingvistično_programiranje) [različne](https://sl.wikipedia.org/wiki/Linearno_programiranje) [stvari](https://en.wikipedia.org/wiki/Broadcast_programming). Pri tem predmetu se bomo učili računalniškega programiranja. Cilj tega je, da računalniku dopovemo, kako naj namesto nas naredi tisto, česar mi ne zmoremo ali preprosto nočemo.

Računalnike programiramo preko _programskih_ jezikov. Tako kot običajni jeziki imajo tudi ti pravila zapisa in pomena, vendar so običajno bolj preprosti in nedvoumni, saj jih morajo poleg ljudi razumeti tudi računalniki. Nekateri programski jeziki so bliže ljudem, drugi bliže računalnikom, vsi pa slonijo na zelo podobnih idejah. Ko znamo programirati v enem, lahko hitro preklopimo na drugega.

## O Pythonu

Pri tem predmetu se bomo naučili jezika Python, ki je precej prijazen do začetnikov, hkrati pa tudi izjemno popularen, zato bo pridobljeno znanje takoj uporabno. Python se imenuje po skupini Monty Python, kar se vidi tudi v dokumentaciji, kjer je precej referenc na njihove skeče. Avtor Pythona je Guido van Rossum, ki je bil do nedavnega tudi BDFL (benevolent dictator for life), torej tisti z zadnjo besedo pri pomembnih odločitvah glede prihodnosti Pythona. Leta 2018 je z mesta odstopil ter nadzor predal skupnosti.

Tudi če vas zgodovina Pythona ne zanima, ji bomo posvetili malo pozornosti, saj se jo je treba zavedati v vsakdanji uporabi. Pythonova prva javna objavljena različica je bil Python 0.9 leta 1991, vendar se je pravi razmah začel šele leta 2000 z različico 2.0\. Kljub nekaj posodobitvam je postalo očitno, da je za prihodnji razvoj potrebno narediti nekaj večjih sprememb, ki bodo jezik prečistile, vendar bodo zaradi njih nekateri programi, napisani v Pythonu 2, prenehali delovati.

Tako je leta 2008 izšel Python 3.0, prva različica Pythona 3, leta 2010 pa Python 2.7 zadnja različica Pythona 2\. Razvijalci Pythona so upali, da bodo avtorji starih programov prešli na Python 3 in napovedali, da bo Python 2 podprt samo še do leta 2015\. Žal pa je bil Python 2 do takrat že tako uveljavljen, da veliko uporabnikov ni želelo opraviti prehoda, zato je bil rok zamaknjen na 1\. januar 2020\. V zadnjih letih so tako vse večje knjižnice in večina uporabnikov prešli na Python 3, vendar Python 2 še vedno živi, zato morate biti pozorni, katero različico uporabljate. Pri tem predmetu bomo uporabljali izključno Python 3, lahko pa se zgodi, da si ponesreči namestite in poženete Python 2, v katerem bodo stvari delovale precej podobno, na vsake toliko časa pa bo neka stvar delovala drugače in vas presenetila.

## Delo s Pythonom

Python najenostavneje uporabljamo prek interaktivne konzole, v katero pišemo ukaze, ki jih računalnik nato izvede ter vrne odgovor. Do interaktivne konzole lahko dostopamo na več načinov: neposredno iz ukazne vrstice, prek okolja IDLE, ki je priloženo vsaki namestitvi Pythona, ali pa iz naprednejšega urejevalnika besedil. V vseh primerih nas pozdravi približno tak izpis:

```
Python 3.7.3 (default, Nov 15 2019, 04:04:52) 
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Na začetku natančno piše, katero različico Pythona uporabljamo. Bodite pozorni, da piše `Python 3.x.x` (zadnji dve številki nista tako ključni), in ne `Python 2.x.x`. Številki različice sledi nekaj kazalcev na osnovne informacije, v zadnji vrstici pa poziv `>>>`, ki kaže, da je računalnik pripravljen na naš vnos.

Za začetek izračunajmo, koliko je 1 + 1\. Vnesemo `1 + 1` ter pritisnimo znak za novo vrstico. Ob tem Python prebere naš vnos, ga izračuna in izpiše rezultat.

```
>>> 1 + 1
2
```

Interaktivna konzola je uporabna za krajše programe, daljše pa raje shranimo v datoteko. S tem preprečimo, da bi izgubili vse svoje delo, pa tudi lažje popravljamo napake, saj nam ni treba vsega ponovno vnašati. Pythonove programe shranjujemo v običajne tekstovne datoteke, kar pomeni, da jih lahko odpremo s katerim koli urejevalnikom besedila. Pythonovim datotekam običajno damo končnico `.py`.

V tem učbeniku bomo uporabljali tretji način in sicer interaktivne zvezke, ki jih ponuja orodje Jupyter. Ti zvezki so sestavljeni iz celic, v katerih se programi izmenjujejo z besedilom. Celicam s programi sledijo celice z odzivom, vse skupaj pa je videti takole:

```{code-cell}
1 + 1
```
