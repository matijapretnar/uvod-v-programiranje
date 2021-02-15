# Nizi

Funkcija, ki vrne ustrezen pozdrav

```python
>>> pozdrav('Matija')
'Dober dan, gospod profesor.'
>>> pozdrav('Anja')
'Pozdravljena, gospa asistentka.'
>>> pozdrav('Filip')
'Pozdravljeni, gospod asistent.'
>>> pozdrav('Francelj')
'Živjo, Francelj!'
```

## Indeksi in rezine

Najdaljši podniz, ki je palindrom

```
>>> max_podpalindrom('otorinolaringolog')
'ooriroo'
>>> max_podpalindrom('ventrilokvist')
'tilit'
>>> max_podpalindrom('neradodaren')
'neradodaren'
```

## Vse v Pythonu je objekt, `__add__`

## Branje in pisanje s konzole

Funkcija `print` **izpiše** dani niz

```
>>> print('Pozdravljen, svet!')
*Pozdravljen, svet!
>>> print('"Grem v rudnik", je rekla.')
*"Grem v rudnik", je rekla.
>>> print("Tole je kr'neki!")   
*Tole je kr'neki!
>>> print('Tole je kr\'neki!')   
*Tole je kr'neki!
>>> print('en\ndva\ntri')
*en
*dva
*tri
```

`print` poleg nizov izpisuje tudi druge vrednosti

```
>>> print(1 + 1)
*2
>>> print(3 + 4 < 5)
*False
```

Izpišemo lahko tudi več vrednosti

```
>>> print('a', 123, None)
*a 123 None
```

Funkcija `print` ne vrne **ničesar**

```
>>> 1 + 1
2
>>> print(1 + 1)
*2
>>> 1 + (1 + 1)
3
>>> 1 + print(1 + 1)
*2
TypeError: unsupported operand type(s)
  for *: 'int' and 'NoneType'
```

Kaj izpiše ukaz `print(print(42))`

Kaj vrne ukaz `print(print(42))`

`print`, `input`

## Pretvorbe med tipi

`str`, `int`, `bool`, v pogojnih stavkih
