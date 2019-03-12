---

class: center, middle
## Vgrajene metode 

---

class: center, middle
## vse v Pythonu je objekt
# objekt ~ podatki + metode

---

### Vgrajene metode na nizih

```python
>>> 'lokomotiva'.count('o')
3
>>> 'lokomotiva'.index('m')
4
>>> '&'.join(['a', 'b', 'c'])
'a&b&c'
>>> 'lokomotiva'.replace('o', 'u')
'lukumutiva'
>>> '  x  y  z  '.strip()
'x  y  z'
>>> 'lokomotiva'.upper()
'LOKOMOTIVA'
>>> 'to je stavek'.split()
['to', 'je', 'stavek']
```

---

### Vgrajene metode na seznamih in naborih

```python
>>> [1, 2, 3, 2, 1, 4, 2].count(2)
3
>>> [1, 2, 3, 2, 1, 4, 2].index(2)
1
>>> [1, 2, 3, 2, 1, 4, 2].index(2, 2)  
3
>>> (1, 2, 3, 2, 1, 4, 2).count(2)
3
>>> (1, 2, 3, 2, 1, 4, 2).index(2)
1
>>> (1, 2, 3, 2, 1, 4, 2).index(2, 2)  
3
```

---

### Z metodo `get` jemljemo vrednosti iz slovarja

```python
>>> s = {'a': 6, 'b': 2, 'c': 3}
>>> s.get('a')
6
>>> s.get('d')
>>> s.get('d', 0)
0
>>> s.get('a', 0)
6
```
