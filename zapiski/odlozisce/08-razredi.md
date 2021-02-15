# Razredi

objekte združujemo v razredih

# objekt ~ podatki + metode

## Objekti v istem razredu imajo različne podatke (atribute) ter enake metode

## Definicije lastnih razredov

Definicija razreda sestoji iz definicij **metod**

```python
class Pes:
    def daj_glas(self, veselje):
        print(veselje * 'hov' + '!')
```

```python
>>> fido = Pes()
>>> fido.daj_glas(10)
hovhovhovhovhovhovhovhovhovhov!
>>> fido.daj_glas(5)
hovhovhovhovhov!
```

V metodah lahko dostopamo do **atributov**

```python
class Pes:
    def vzpostavi_zacetno_veselje(self):
        self.veselje = 1
    def daj_glas(self):
        print(self.veselje * 'hov' + '!')
    def razveseli(self):
        self.veselje += 1
```

```python
>>> fido = Pes()
>>> fido.vzpostavi_zacetno_veselje()
>>> fido.razveseli()
>>> fido.daj_glas()
hovhov!
```

**Začetne atribute** nastavimo z `__init__`

```python
class Pes:
    def __init__(self):
        self.veselje = 1
    def daj_glas(self):
        print(self.veselje * 'hov' + '!')
    def razveseli(self):
        self.veselje += 1
```

```python
>>> fido = Pes()
>>> fido.daj_glas()
hov!
>>> fido.razveseli()
>>> fido.daj_glas()
hovhov!
```

Ustvarimo lahko tudi **več objektov**

```python
>>> fido = Pes()
>>> fido.razveseli()
>>> runo = Pes()
>>> fido.daj_glas()
hovhov!
>>> runo.daj_glas()
hov!
```

Konstruktorjem lahko podamo argumente

```python
class Pes:
  def __init__(self, glas='hov'):
    self.veselje = 1
    self.glas = glas
  def daj_glas(self):
    print(self.veselje * self.glas + '!')
  def razveseli(self):
    self.veselje += 1
```

```python
>>> fido = Pes(glas='vuf')
>>> fido.razveseli()
>>> fido.daj_glas()
vufvuf!
```

atributi, metode, `self`

## Posebne metode

Za **prikaz v konzoli** uporabljamo `__repr__`

```python
class Pes:
    ...
```

```python
>>> fido = Pes()
>>> fido
<__main__.Pes object at 0x107a98b70>
```

Za **prikaz v konzoli** uporabljamo `__repr__`

```python
class Pes:
    ...
    def __repr__(self):
        return 'Pes(glas={0!r})'.format(
            self.glas
        )
    ...
```

```python
>>> fido = Pes()
>>> fido
Pes(glas='hov')
```

Za **človeški izpis** uporabljamo `__str__`

```python
class Pes:
    ...
    def __str__(self):
        return 'Pes, ki dela {0}.'.format(
            self.glas
        )
    ...
```

```python
>>> fido = Pes()
>>> print(fido)
Pes, ki dela hov.
```

Za **vsoto** uporabljamo `__add__`

```python
class Pes:
  ...
  def __add__(self, other):
    od_mame = self.glas[:len(self.glas) // 2]
    od_ata = other.glas[len(other.glas) // 2:]
    return Pes(glas=(od_mame + od_ata))
  ...
```

```python
>>> reks = Pes(glas='hov')
>>> lajka = Pes(glas='vuf')
>>> lajka + reks
Pes(glas='vov')
```

Podobno imamo metode `__sub__`, `__mul__`, ...

## Statične in razredne metode

## `property`

## Dedovanje

## Zgoščevalne tabele

- defaultdict
