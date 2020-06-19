# Tekstovni vmesnik

## Ločitev modela in vmesnika

Programov se splača lotiti **od zgoraj navzdol**

```
def vislice():
    igra = nova_igra()
    while not konec(igra):
        igra = ugani_crko(igra)

def nova_igra():
    ...
def konec(igra):
    ...
def ugani_crko(igra):
    ...

vislice()
```

Dobro je, da sta **model in vmesnik ločena**

```
def ugani_crko(igra):
    crka = input('Vpiši črko:')
    pravilno = crka in igra.geslo
    if pravilno:
        print('Bravo!')
    else:
        print('Narobe!')
        obesen += 1
    igra.odkrite.add(crka)
```

Kaj bomo morali spremeniti za spletni vmesnik?

```
def ugani_crko_model(igra, crka):
    igra.odkrite.add(crka)
    pravilno = crka in igra.geslo
    if not pravilno:
        obesen += 1
    return pravilno

def ugani_crko_vmesnik(igra):
    crka = input('Vpiši črko:')
    if ugani_crko_model(igra, crka):
        print('Bravo!')
    else:
        print('Narobe!')
```

Model je običajno svoj **razred**

```
class Igra:
  def ugani_crko(self, crka):
    self.odkrite.add(crka)
    pravilno = crka in self.geslo
    if not pravilno:
        obesen += 1
    return pravilno

def ugani_crko_vmesnik(igra):
    crka = input('Vpiši črko:')
    if igra.ugani_crko(crka):
        print('Bravo!')
    else:
        print('Narobe!')
```

## Lokalne knjižnice, zasebne metode

## Strukturiranje tekstovnega vmesnika

top-down funkcije, pomožne funkcije

## Shranjevanje stanja

## Knjižnica `datetime`
