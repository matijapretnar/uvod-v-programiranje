`random.random()` vrne naključno realno število na intervalu `[0, 1]`

```python
for _ in range(10):
    print(random.random())
```

```python
0.269454709396
0.150338688416
0.86826547468
0.645895807098
0.772181460437
0.522534622302
0.472586885944
0.0620787396277
0.913226625841
0.248149046053
```

`random.uniform(a, b)` vrne naključno realno število na intervalu `[a, b]`

```python
for _ in range(10):
    print(random.uniform(10, 15))
```

```python
12.8787811514
12.6687121738
12.1844239968
11.1800356184
13.2297206416
10.4020532268
14.9780516491
13.1393786622
14.3589751972
12.4133107171
```

`random.randint(a, b)` vrne naključno naravno število na intervalu `[a, b]`

```python
for _ in range(10):
    print(random.randint(10, 15))
```

```python
10
15
14
12
12
12
13
11
11
10
```

`random.randrange(a, b)` vrne naključno naravno število na intervalu `[a, b)`

```python
for _ in range(10):
    print(random.randrange(10, 15))
```

```python
14
11
11
14
14
11
14
13
10
14
```

`random.choice(elementi)` vrne naključno izbran element

```python
for _ in range(10):
    print(random.choice([1, 10, 50]))
```

```python
1
50
1
50
50
1
10
10
1
1
```

`random.choice(elementi)` vrne naključno izbran element

```python
for _ in range(10):
    print(random.choice('abc'))
```

```python
b
c
b
b
c
a
a
c
b
b
```

`random.sample(elementi, k)` vrne `k` naključno izbranih elementov

```python
for _ in range(10):
    print(random.sample('abcdefg', 3))
```

```python
['f', 'd', 'g']
['g', 'a', 'd']
['f', 'g', 'e']
['b', 'f', 'a']
['g', 'c', 'd']
['g', 'c', 'a']
['b', 'f', 'c']
['b', 'f', 'a']
['g', 'f', 'e']
['d', 'g', 'e']
```

`random.shuffle` naključno premeša seznam

```python
>>> seznam = [10, 20, 30, 40, 50]
>>> random.shuffle(seznam)
>>> seznam
[30, 20, 40, 10, 50]
```

## Met poštenega kovanca

```python
for _ in range(10):
    print(posteni_kovanec())
```

```python
cifra
grb
grb
cifra
cifra
cifra
grb
grb
grb
cifra
```

## Met nepoštenega kovanca

```python
for _ in range(10):
    print(neposteni_kovanec(0.2))
```

```python
cifra
cifra
grb
cifra
cifra
cifra
cifra
grb
cifra
cifra
```

Met nepoštene kocke

## Kako generiramo naključne vrednosti?

background-image: url(slike/generator.jpg)

Cenejši način je uporaba psevdonaključnih števil

```
1234

<sup>2</sup>

 = 01**5227**56
5227

<sup>2</sup>

 = 27**3215**29
3215

<sup>2</sup>

 = 10**3362**25
3362

<sup>2</sup>

 = 11**3030**44
3030

<sup>2</sup>

 = 09**1809**00
```

Začetnemu številu pravimo seme

Seme lahko nastavimo z `random.seed`

```python
>>> random.seed(3)
>>> random.random()
0.23796462709189137
>>> random.random()
0.5442292252959519
>>> random.seed(3)
>>> random.random()
0.23796462709189137
>>> random.random()
0.5442292252959519
```

## Generator psevdonaključnih števil

## Linearni kongruenčni generator

background-image: url(slike/generator.jpg)

Izračun števila (\pi)

V 28 metih kovanca je padlo 20 cifer. Je kovanec pošten?

Kako bi se lahko izognili razmišljanju?
