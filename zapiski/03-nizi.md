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

# Nizi

V programih seveda ne delamo le s števili, temveč tudi z drugimi podatki, na primer besedili. V ta namen Python podpira nize, ki so strnjena zaporedja znakov. Nize običajno pišemo v enojnih narekovajih, na primer `'to je primer niza'`.

## Osnovne operacije na nizih

Nize lahko stikamo z operacijo `+` in množimo s celimi števili:

```{code-cell}
'zala' + 'gasper'
```

```{code-cell}
'tro' + 4 * 'lo'
```

Dolžino niza dobimo s funkcijo `len`:

```{code-cell}
len('lokomotiva')
```

Nize lahko med seboj tudi primerjamo. Pri tem Python nize ureja leksikografsko, torej tako, kot bi bili urejeni v leksikonu ali kazalu: najprej primerja prvi črki, če sta ti dve enaki, pogleda drugi dve, in tako naprej. Pri tem velike črke pridejo na vrsto pred malimi, na šumnike pa se brez posebnih knjižnic Python ne spozna.

```{code-cell}
'beseda' == 'konj'
```

```{code-cell}
'abak' <= 'abeceda'
```

Na nizih imamo na voljo tudi predikat `in`, s katerim ugotovimo, ali se nek niz pojavlja kot podniz v drugem nizu. Na voljo je tudi `not in`, s katerim bolj berljivo zapišemo ravno nasprotno stvar:

```{code-cell}
'gram' in 'Uvod v programiranje'
```

```{code-cell}
'liter' in 'Uvod v programiranje'
```

```{code-cell}
not ('liter' in 'Uvod v programiranje')
```

```{code-cell}
'liter' not in 'Uvod v programiranje'
```

## Indeksi in rezine

Do posameznega znaka v nizu pridemo z _indeksi_. Z izrazom `niz[i]` dostopamo do `i`-tega znaka v danem nizu:

```{code-cell}
'REKURZIJA'[3]
```

```{code-cell}
'REKURZIJA'[0]
```

```{code-cell}
'REKURZIJA'[-1]
```

Indeksi se začnejo šteti z 0\. Če uporabimo negativna števila, lahko štejemo tudi od zadaj, vendar tam začnemo šteti z -1 (saj je -0 = 0).

```
\ 0   1   2   3   4   5   6   7   8
 R   E   K   U   R   Z   I   J   A
-9  -8  -7  -6  -5  -4  -3  -2  -1
```

Na podoben način lahko dostopamo tudi do podnizov. Če napišemo `niz[i:j]` bomo dobili niz, ki mu pravimo _rezina_ in sega od vključno `i`-tega do vključno `j - 1`-tega znaka. Če kakšno od meja izpustimo, bomo vzeli vse znake od začetka oziroma do konca.

```{margin}
Videli bomo, da razpon od $i$ do $j$ v Pythonu pogosto pomeni vse od vključno $i$ do vključno $j - 1$. To je malo neobičajno, vendar ima nekaj prednosti: razpon od $i$ do $j$ vedno vsebuje $j - i$ elementov, hkrati pa lahko razpone sestavljamo brez prekrivanja. Na primer, `niz[i:j] + niz[j:k]` je enako kot `niz[i:k]` (vsaj, če velja `i < j < k`).
```

```{code-cell}
'REKURZIJA'[2]
```

```{code-cell}
'REKURZIJA'[6]
```

```{code-cell}
'REKURZIJA'[2:6]
```

```{code-cell}
'REKURZIJA'[:6]
```

```{code-cell}
'REKURZIJA'[2:]
```

Pišemo lahko tudi `niz[i:j:k]`, s čimer vzamemo le vsak `k`-ti znak:

```{code-cell}
'REKURZIJA'[1:8]
```

```{code-cell}
'REKURZIJA'[1:8:1]
```

```{code-cell}
'REKURZIJA'[1:8:2]
```

```{code-cell}
'REKURZIJA'[1:8:3]
```

```{code-cell}
'REKURZIJA'[::-1]
```

S pomočjo indeksov in rezin lahko napišemo (ne najbolj učinkovito) funkcijo, ki prešteje vse samoglasnike v danem nizu:

```{code-cell}
def stevilo_samoglasnikov(niz):
    if niz == '':
        return 0
    elif niz[0] in 'aeiouAEIOU':
        return 1 + stevilo_samoglasnikov(niz[1:])
    else:
        return stevilo_samoglasnikov(niz[1:])

stevilo_samoglasnikov('Uvod v programiranje')
```

Funkcija deluje tako, da najprej pogleda, če je niz prazen. Če je, v njem ni samoglasnikov, zato vrne 0\. Če ni, pogleda prvi znak. Če je samoglasnik, potem je število samoglasnikov za ena večje od števila samoglasnikov v preostanku niza (ki ga dobimo s pomočjo rezine), sicer pa je enako številu samoglasnikov v preostanku.

## Zapisi nizov

Nize lahko pišemo tudi z dvojnimi narekovaji, ki jih ponavadi uporabimo takrat, kadar v nizu želimo uporabiti enojni narekovaj: `"Tole je kr'neki!"`. V tem primeru niza ne moremo pisati med enojnimi narekovaji, saj bi Python po narekovaju za `kr` mislil, da je konec niza.

```{code-cell}
:tags: ["raises-exception"]
'Tole je kr'neki!'
```

Včasih želimo uporabiti obe vrsti narekovajev. V tem primeru si pomagamo z _ubežnimi znaki_. To so znaki, ki jih na običajni način ne moremo zapisati, zato uporabimo poseben zapis, ki se začne z znakom `\`. Tedaj lahko pišemo `'"Tole je kr'neki," je rekla.'` ali pa `"\"Tole je kr'neki,\" je rekla.\"`. Ubežne znake brez težav lahko pišemo tudi tedaj, kadar ni treba `'\"Grem v rudnik,\" je rekla.'`. Z ubežnimi znaki lahko zapišemo tudi znak za novo vrstico `\n`, za tabulator `\t` in seveda tudi za poševnico `\\`, saj je ne moremo pisati le kot `\`, ker bi Python to razumel kot začetek ubežnega znaka.

Nize lahko pišemo tudi med tri enojne (`'''`) ali tri dvojne (`"""`) narekovaje (ki smo jih videli že pri dokumentacijskem nizu). V tem primeru za en sam narekovaj ne potrebujemo ubežnega znaka. Take nize lahko pišemo tudi čez več vrstic.

Različni zapisi ne vplivajo na vsebino. Tako `'"Živjo!"'`, `'\"Živjo!\"'`,`"\"Živjo!\""`, `'''"Živjo!"'''` ali `""""Živjo!\""""` vsi predstavljajo enak niz z osmimi znaki.

## Vgrajene metode na nizih

```{margin}
Kdaj se uporablja funkcije in kdaj metode?

TODO
```

Precej operacij na nizih pa lahko opravimo preko _metod_. To so funkcije, ki jih na poseben način kličemo na posamezni vrednosti. Na primer, za pretvarjanje niza v male črke pokličemo

```{code-cell}
'REKURZIJA'.lower()
```

Klic metod na nizih ima splošno obliko `niz.metoda(...)`, kjer v oklepajih naštejemo argumente. Na primer, pojavitve posameznega znaka v nizu preštejemo z metodo `count`:

```{code-cell}
niz = 'Otorinolaringolog'
niz.count('o')
```

Klice metod lahko tudi verižimo:

```{code-cell}
niz = 'Otorinolaringolog'
niz.lower().count('o')
```

Vse metode, ki so na voljo na nizih lahko najdete v [uradni dokumentaciji](https://docs.python.org/3/library/stdtypes.html#string-methods), zato naštejmo le najbolj pogosto uporabljane:

- `s.count(t)` vrne število pojavitev podniza `t` v nizu `s`. Klic `s.count(t, i)` deluje podobno, le da začne šteti šele pri indeksu `i`, klic `s.count(t, i, j)` pa konča šteti pri indeksu `j`.

- `s.index(t)` vrne najmanjši indeks v nizu `s`, kjer se niz `t` pojavi kot podniz. Podobno kot prej klic `s.index(t, i)` začne iskati pri indeksu `i`, klic `s.index(t, i, j)` pa konča pri indeksu `j`. Če niza ni, metoda sproži napako. Metoda `s.find` se obnaša enako kot `s.index`, le da v primeru, ko podniza ne najde, vrne `-1`.

- `s.join(sez)` z ločilom `s` skupaj stakne vse nize iz seznama `sez` (te bomo spoznali {ref}`kmalu <seznami-in-nabori>`).

- `s.replace(t1, t2)` vrne niz `s`, v katerem smo vse pojavitve podniza `t1` zamenjali s podnizi `t2`. Klic `s.replace(t1, t2, n)` pa zamenja le prvih `n` pojavitev.

- `s.strip()` vrne niz `s`, v katerem smo odstranili vse bele znake (presledke, tabulatorje, nove vrstice) z začetka in konca. Klic `s.strip(t)` z začetka in konca odstrani vse znake iz niza `t`.

- `s.lower()` / `s.upper()` / `s.title()` / `s.capitalize()` / `s.swapcase()` vrnejo niz `s`, v katerem smo vse črke zamenjali z malimi / vse črke zamenjamo z velikimi / vsem besedam damo veliko začetnico / na začetku niza damo veliko začetnico / male črke zamenjamo z velikimi in obratno.

- `s.split()` vrne seznam besed v nizu `s` (ločene glede na bele znake). Klic `s.split(t)` loči glede na podniz `t`. Klic `s.split(t, n)` vrne niz razbit na prvih `n` ločilih.

- `s.isdigit()` / `s.isalpha()` / `s.islower()` / `s.isupper()` / `s.isalnum()` / `s.isspace()` vrnejo `True` natanko takrat, kadar je niz `s` neprazen in so vsi znaki števke / črke / male črke / velike črke / črke ali številke / beli znaki.

## `f`-nizi

Včasih je bila v Pythonu zelo uporabna tudi metoda `format`. Ta vzame niz, v katerem so z zavitimi oklepaji označeni prostori, ki jih zapolnimo z argumenti metode. Na primer

```{code-cell}
'{0} ima {1}'.format('mama', 'stol')
```

ali pa

```{code-cell}
niz = '{0} vzklika: "{1}, {1}, {1}!"'
niz.format('Mama', 'joj')
```

```{code-cell}
niz.format('Tone', 'FMF')
```

Argumente lahko tudi oblikujemo in poimenujemo, kar je razloženo v [uradni dokumentaciji](https://docs.python.org/3/library/string.html#format-string-syntax). Po novem, od Pythona 3.6 naprej, pa lahko uporabljamo tudi _`f`-nize_. To so nizi, ki jih na začetku označimo z znakom `f`, nato pa v zavite oklepaje zapišemo vrednost, ki naj jo Python izračuna in vstavi v niz. Na primer:

```{code-cell}
kdo = 'Mama'
kaj = 'joj'
f'{kdo} vzklika: "{kaj}, {kaj}, {kaj}!"'
```

ali pa

```{code-cell}
a, b = 22, 7
f'{a}/{b} = {a / b:.5}'
```

Tako kot pri metodi `format` lahko tudi pri `f`-nizih izračunane vrednosti oblikujemo:

```{code-cell}
a, b = 22, 7
f'{a}/{b} = {a / b:.5}'
```

```{code-cell}
f'popust znaša {1 / 3:.2%}'
```

```{code-cell}
f'{"NASLOV":*^30}'
```

Možnosti za oblikovanje je veliko, vse pa so opisane v [uradni dokumentaciji](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).

## Pisanje na konzolo in branje s konzole

TODO
