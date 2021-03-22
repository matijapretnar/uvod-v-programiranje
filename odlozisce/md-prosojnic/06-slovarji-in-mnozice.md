# Knjižnica `collections`

# Zanka `for`

```
knjiga_obrazov = {
    'Anka': {'Bogomir', 'Cvetka'},
    'Bogomir': {'Cvetka', 'Dragomir'},
    'Cvetka': {'Anka'},
    'Dragomir': {'Anka', 'Cvetka'},
}
```

priporocila(knjiga_obrazov, 'Bogomir')

priporocila(knjiga_obrazov, 'Cvetka')

# Množice

```python
{1, 2, 3, 4}    set()
```

```
def je_prastevilo(n):

:   

    if n <= 2:

    :   return n == 2

    d = 3 while d * d <= n: if n % d == 0: return False d += 2 return
    True
```

```
majhna_prastevila = {2, 3, 5, 7, ..., 997}

def je_prastevilo(n):
    if n <= majhna_prastevila[-1]:
        return n in majhna_prastevila
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
```
