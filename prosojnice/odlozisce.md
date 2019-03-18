class: middle, question

```
>>> najvecji_element([-5, 2, 10, -13, 0])
10
>>> najvecji_element([])
```

```
>>> najdaljsi_podseznam([[1, 2], [3, 4, 5], [6]])
[3, 4, 5]
>>> najdaljsi_podseznam([])
>>> najdaljsi_podseznam([[1, 2, 3], [4, 5, 6]])
[1, 2, 3]
```

```
>>> absolutno_najvecji([-5, 2, 10, -13, 0])
-13
>>> absolutno_najvecji([])
>>> absolutno_najvecji([10, 20, 30, -40])
-40
```

---

class: center, middle

## Pretvorbe med tipi

---

### V **nize** pretvarjamo s funkcijo `str`

```python
>>> str(True)
'True'
>>> str(10)
'10'
>>> str([1, 2, 3])
'[1, 2, 3]'
>>> str(['a', 'b', 'c'])
"['a', 'b', 'c']"
>>> str('abc')
'abc'
```

---

### V **Booleove vrednosti** pretvarjamo z `bool`

```python
>>> bool(1)
True
>>> bool('niz')
True
>>> bool('')
False
>>> bool(0)
False
>>> bool([])
False
>>> bool('False')
True
>>> bool([0, 0, 0])
True
```

---

### Pogojni stavek **samodejno pretvori** z `bool`

```python
if n != 0:
    ...
```

```python
if niz != '':
    ...
```

```python
if sez != []:
    ...
```

---

### Pogojni stavek **samodejno pretvori** z `bool`

```python
if n:
    ...
```

```python
if niz:
    ...
```

```python
if sez:
    ...
```

---

### V cela števila pretvarjamo s funkcijo `int`
```python
>>> int('123')
123
>>> int(5.213)
5
>>> int('osem')
...
ValueError: invalid literal
  for int() with base 10: 'osem'
>>> int('5.213')
...
ValueError: invalid literal
  for int() with base 10: '5.213'
```

---

### V sezname pretvarjamo s funkcijo `list`
```python
>>> list('abc')
['a', 'b', 'c']
>>> list()
[]
>>> list((1, 2, 3))
[1, 2, 3]
>>> list({'a', 'b', 'c'})
['b', 'a', 'c']
```

---

### V nabore pretvarjamo s funkcijo `tuple`
```python
>>> tuple('abc')
('a', 'b', 'c')
>>> tuple()
()
>>> tuple([1])
(1,)
>>> tuple({1, 2, 3})
(1, 2, 3)
```

---

### V množice pretvarjamo s funkcijo `set`
```python
>>> set('abc')
{'b', 'c', 'a'}
>>> set('abcabcabc')
{'b', 'c', 'a'}
>>> set()
set()
>>> set([1])
{1}
>>> set({1: 'a', 2: 'b'})
{1, 2}
```

---

### V slovarje pretvarjamo s funkcijo `dict`
```python
>>> dict([(1, 2), (3, 4)])
{1: 2, 3: 4}
>>> dict()
{}
```
