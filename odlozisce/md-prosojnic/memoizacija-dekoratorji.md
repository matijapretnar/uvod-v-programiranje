### Slovarje lahko uporabimo za **memoizacijo**

```
kvadrati = {}
def mem_kvadrat(x):
    if x not in kvadrati:
        print('Računam', x)
        y = x ** 2
        kvadrati[x] = y
    return kvadrati[x]
```

```
>>> mem_kvadrat(10)
Računam 10
100
>>> mem_kvadrat(10)
100
```

---

class: question

## Število vseh stolpov iz danih kock

.small.center[![](../02-rekurzija/slike/stolpi.png)]

```
>>> stevilo_stolpov(2)
2
>>> stevilo_stolpov(4)
7
```

---

### Memoizacija s **funkcijo višjega reda**

```
def memoiziraj(f):
    rezultati = {}
    def mem_f(x):
        if x not in rezultati:
            rezultati[x] = f(x)
        return rezultati[x]
    return mem_f
```

---

### V Pythonu lahko definicije **dekoriramo**

```
def f(x):
    ...

f = deko(f)
```

```
@deko
def f(x):
    ...
```

---

class: question, middle

```
@povej_kaj_racunas
def kvadriraj(x):
    return x ** 2
```

```
>>> kvadriraj(4)
Računam 4
16
>>> kvadriraj(5)
Računam 5
25
```

---

### Memoizacija z **dekoratorjem**

```
@memoiziraj
def fib(n):
    print(n, end='')
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
```

```
>>> fib(10)
10987654321055
>>> fib(10)
55
```
