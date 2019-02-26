---

### V Pythonu lahko delamo tudi z nizi

```
>>> 'Dober' + 'dan'
'Doberdan'
>>> 'tro' + 4 * 'lo'
'trololololo'
>>> len('lokomotiva')
10
>>> 'beseda' == 'konj'
False
>>> 'abak' <= 'abeceda'
True
>>> 'gram' in 'Uvod v programiranje'
True
```

---

class: question

## Funkcija, ki vrne ustrezen pozdrav

```
>>> pozdrav('Matija')
'Dober dan, gospod profesor.'
>>> pozdrav('Žiga')
'Pozdravljeni, gospod asistent.'
>>> pozdrav('Anja')
'Pozdravljena, gospa asistentka.'
>>> pozdrav('Francelj')
'Živjo, Francelj!'
```

---

### Po potrebi uporabljamo različne narekovaje

.bad-example[```
>>> 'Tole je kr'neki!'
                   ^
SyntaxError: invalid syntax
```]

```
>>> "Tole je kr'neki!"
"Tole je kr'neki!"
>>> '"Grem v rudnik," je rekla.'
'"Grem v rudnik," je rekla.'
>>> '''"Tole je kr'neki," je rekla.'''
'"Tole je kr\'neki," je rekla.'
>>> 'niz' == "niz"
True
>>> 'niz' + "niz" + '''niz''' + """niz"""
'nizniznizniz'
```

---

### Do posameznih znakov dostopamo z **indeksi**

```
>>> 'rekurzija'[3]
'u'
>>> 'rekurzija'[0]
'r'
>>> 'rekurzija'[-1]
'a'
```

```
 0   1   2   3   4   5   6   7   8
 R   E   K   U   R   Z   I   J   A
-9  -8  -7  -6  -5  -4  -3  -2  -1
```

---

### Do več znakov dostopamo z **rezinami**

```
>>> 'rekurzija'[2]
'k'
>>> 'rekurzija'[6]
'i'
>>> 'rekurzija'[2:6]
'kurz'
>>> 'rekurzija'[:6]
'rekurz'
>>> 'rekurzija'[2:]
'kurzija'
```

---

### Rezinam lahko določimo velikost koraka

```
>>> 'rekurzija'[1:8]
'ekurzij'
>>> 'rekurzija'[1:8:1]
'ekurzij'
>>> 'rekurzija'[1:8:2]
'euzj'
>>> 'rekurzija'[1:8:3]    
'erj'
>>> 'rekurzija'[::-1]
'ajizruker'
```

---

class: question

## Število samoglasnikov

```
>>> stevilo_samoglasnikov('Uvod v programiranje')
7
>>> stevilo_samoglasnikov('čmrlj')
0
>>> stevilo_samoglasnikov('otorinolaringolog')
8
```

---

class: question

## Najdaljši podpalindrom

```
>>> najdaljsi_podpalindrom('otorinolaringolog')
'ooriroo'
>>> najdaljsi_podpalindrom('ventrilokvist')
'tilit'
>>> najdaljsi_podpalindrom('neradodaren')
'neradodaren'
```

---

### Funkcija `print` **izpiše** dani niz

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

---

### `print` poleg nizov izpisuje tudi druge vrednosti

```
>>> print(1 + 1)
*2
>>> print(3 + 4 < 5)
*False
```

### Izpišemo lahko tudi več vrednosti

```
>>> print('a', 123, None)
*a 123 None
```

---

### Funkcija `print` ne vrne **ničesar**

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
