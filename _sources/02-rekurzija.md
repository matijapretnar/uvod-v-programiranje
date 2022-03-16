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

# Rekurzija

Videli smo, da probleme rešujemo s prevajanjem na manjše, dokler ne pridemo do čisto osnovnih. Na primer, površino tetraedra izračunamo iz ploščin trikotnikov, te pa lahko prevedemo na vgrajene aritmetične operacije.

Dostikrat pa bodo manjši problemi iste oblike kot prvotni problem. Poglejmo, kako bi izračunali $n! = n \cdot (n - 1) \dots 3 \cdot 2 \cdot 1$. Kot vidimo velja $n! = n \cdot (n - 1)!$, zato bomo $n!$ izračunali tako, da bomo $n$ pomnožili z $(n - 1)!$. Toda od kod bomo dobili tega? Preprosto, $n - 1$ bomo pomnožili z $(n - 2)!$. Od kod pa tega? Ja iz $(n - 3)!$. In tako naprej vse do $2!$, ki ga bomo dobili iz $1!$, tega pa iz $0!$, ki je po definiciji enak $1$. Torej lahko funkcijo, ki računa fakulteto, napišemo tako, da najprej pogleda svoj argument `n`. Če je enak 1, vrne 1, sicer pa `n` pomnožimo z rezultatom klica `fakulteta(n - 1)`:

```{code-cell}
def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n - 1)
```

ali s pogojnim izrazom kot:

```{code-cell}
def fakulteta(n):
    return 1 if n == 0 else n * fakulteta(n - 1)
```

```{code-cell}
fakulteta(1)
```

```{code-cell}
fakulteta(5)
```

```{code-cell}
fakulteta(10)
```

Funkcijam, ki so definirane s pomočjo same sebe pravimo, da so _rekurzivne_. Izkaže se, da lahko s pomočjo rekurzije napišemo **čisto vse** izračunljive funkcije na celih številih: ugotovimo lahko, katera števila so praštevila, katera so si prijateljska, katera so popolna, ...

Še en primer rekurzivne definicije so Fibonaccijeva števila. Velja $F_0 = 0$, $F_1 = 1$, za vse $n \ge 2$ pa velja in $F_{n} = F_{n - 1} + F_{n - 2}$. Funkcijo tedaj napišemo podobno na podoben način kot zgornjo: če je `n` enak 0, vrnemo 0, sicer pogledamo, ali je enak 1\. V tem primeru vrnemo 1\. Če pa tudi 1 ni enak, mora biti večji ali enak 2, zato se pokličemo rekurzivno.

```{code-cell}
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

```{code-cell}
fibonacci(3)
```

```{code-cell}
fibonacci(4)
```

```{code-cell}
fibonacci(5)
```

```{code-cell}
fibonacci(20)
```

Kaj se zgodi, če poskušate izračunati `fibonacci(35)`? Po nekaj časa res dobite pravilen odgovor 9227465, vendar to kaže, da nekaj ni v redu. Težava je, da se pri `fibonacci(35)` funkcija pokliče dvakrat: enkrat na 34 in enkrat na 33\. Tudi vsak od teh dveh klicev povzroči dva nadaljnja klica in tako naprej, vse dokler ne pridemo do 0 ali 1\. Bolje bi bilo, če bi jo zastavili malo drugače.

Poleg Fibonaccijevega zaporedja, ki se začne s številoma 0 in 1, obstaja tudi splošno Fibonaccijevo zaporedje, ki se začne s poljubnima členoma $a$ in $b$:

$$a, b, a + b, b + (a + b) = a + 2 b, (a + b) + (a + 2 b) = 2 a + 3 b, \ldots$$

Vidimo, da je $n$. člen tega zaporedja ravno $n - 1$. člen zaporedja, ki se začne s členoma $b$ in $a + b$. Tedaj lahko definiramo:

```{code-cell}
def splosni_fibonacci(n, a=0, b=1):
    """Vrne n-ti člen zaporedja a, b, a + b, a + 2 b, …"""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return splosni_fibonacci(n - 1, b, a + b)
```

Kot lahko sami preizkusimo, ta funkcija deluje veliko hitreje od prejšnje:

```{code-cell}
splosni_fibonacci(35, 0, 1)
```

```{code-cell}
splosni_fibonacci(35, 0, 10)
```

Pomembno ni torej samo to, da naš program pravilno izračuna iskani rezultat, temveč tudi to, kako učinkovito ga izračuna.

Ker smo argumentoma `a` in `b` v definiciji podali privzeti vrednosti, nam jih pri klicu ni treba podati:

```{code-cell}
splosni_fibonacci(35)
```

## Evklidov algoritem

Algoritem je zaporedje korakov, s katerimi dobimo iskani rezultat. Načeloma lahko pod besedo algoritem razumemo tudi zaporedje korakov, s katerimi si skuhamo jajca (vzemi posodo; odpri pipo; postavi posodo pod pipo; ko je posoda dovolj polna, zapri pipo; ...), ampak mi si jo bomo prihranili za postopke, s katerimi izračunamo želene vrednosti.

Za prvi algoritem se spodobi, da si pogledamo najstarejši znani algoritem in sicer Evklidov algoritem za iskanje največjega skupnega delitelja dveh števil. Naj bo $d$ največji skupni delitelj števil $m$ in $n$. Pišimo $m = k \cdot n + o$, kjer je $0 \le o < n$. Torej: $o$ je ostanek pri deljenju števila $m$ z $n$. Ker e $d$ deli $n$, deli tudi $k \cdot n$. Poleg tega $d$ deli tudi $m$, zato deli tudi $o = m - k \cdot n$. Velja tudi obratno, če $d$ deli $n$ in $o$, potem deli tudi $m = k \cdot n + o$.

Zato lahko iskanje največjega skupnega delitelja števil $m$ in $n$ prevedemo na iskanje največjega skupnega delitelja števil $n$ in $o$. Videti je, kot da se vrtimo v krogu, vendar se ne. Poglejmo, kaj se zgodi:

1. Največji skupni delitelj števil $456$ in $123$ je enak največjemu skupnemu delitelju števil $123$ in $456 - 3 \cdot 123 = 87$.
2. Največji skupni delitelj števil $123$ in $87$ je enak največjemu skupnemu delitelju števil $87$ in $123 - 1 \cdot 87 = 36$.
3. Največji skupni delitelj števil $87$ in $36$ je enak največjemu skupnemu delitelju števil $36$ in $123 - 2 \cdot 36 = 15$.
4. Največji skupni delitelj števil $36$ in $15$ je enak največjemu skupnemu delitelju števil $15$ in $36 - 2 \cdot 15 = 6$.
5. Največji skupni delitelj števil $15$ in $6$ je enak največjemu skupnemu delitelju števil $6$ in $15 - 2 \cdot 6 = 3$.
6. Največji skupni delitelj števil $6$ in $3$ je enak največjemu skupnemu delitelju števil $3$ in $6 - 2 \cdot 3 = 0$.

Postopka ne moremo več nadaljevati, ker ne moremo deliti z nič. Kaj pa je največji skupni delitelj števil 3 in 0? Ja, 3 vendar. Torej, ko je drugo število enako 0, je prvo število ravno njun največji skupni delitelj, po vseh prejšnjih sklepih pa tudi največji skupni delitelj vseh prejšnjih parov vključno s prvim.

Evklidov algoritem je torej sledeč: če je $n = 0$, potem je največji skupni delitelj števil $m$ in $n$ enak kar $m$, sicer pa je enak največjemu skupnemu delitelju števil $n$ in $o$, kjer je $o$ ostanek pri deljenju $m$ z $n$. Ta postopek enostavno prevedemo v Python:

```{code-cell}
def gcd(m, n):
    if n == 0:
        return m
    else:
       return gcd(n, m % n)
```

ali s pogojnim izrazom kot

```{code-cell}
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)
```

Pri tem je `gcd` (_greatest common divisor_) običajna oznaka za največjega skupnega delitelja.

```{code-cell}
gcd(456, 123)
```

Algoritem deluje tudi, kadar je $n < m$, saj je v tem primeru $n = 0 \cdot m + n$, zato v naslednjem koraku njuni mesti zamenjamo in nadaljujemo kot prej.

```{code-cell}
gcd(123, 456)
```
