# Git

## Spremembe in repozitoriji

Osnovni izrazi, uporabljeni v Gitu

![](slike/git/commit.png)

### Sprememba (commit)

Zabeleženo stanje datotek skupaj s časom, avtorjem, opisom, podatkih o predhodnikih, ...

### Repozitorij (repository)

Zbirka zabeleženih sprememb.

## Sinhronizacija

Repozitorij kloniramo z ukazom `clone`

.center.git[ ![blank](slike/git/blank.png)

<span class="command">&lt;- clone &lt;-</span>

![initial](slike/git/initial.png)

<span class="command">
</span>

![blank](slike/git/blank.png) ] Repozitorij kloniramo z ukazom `clone`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">&lt;- clone &lt;-</span>

![initial](slike/git/initial.png)

<span class="command">
</span>

![blank](slike/git/blank.png) ] Repozitorij kloniramo z ukazom `clone`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">
</span>

![initial](slike/git/initial.png)

<span class="command">
</span>

![blank](slike/git/blank.png) ] Repozitorij kloniramo z ukazom `clone`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">
</span>

![initial](slike/git/initial.png)

<span class="command">-&gt; clone -&gt;</span>

![blank](slike/git/blank.png) ] Repozitorij kloniramo z ukazom `clone`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">
</span>

![initial](slike/git/initial.png)

<span class="command">-&gt; clone -&gt;</span>

![initial](slike/git/initial.png) ] Spremembo zabeležimo z ukazom `commit`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">
</span>

![initial](slike/git/initial.png)

<span class="command">commit =&gt;</span>

![initial](slike/git/initial.png) ] Spremembo zabeležimo z ukazom `commit`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">
</span>

![initial](slike/git/initial.png)

<span class="command">commit =&gt;</span>

![commit](slike/git/commit.png) ] Spremembe na strežnik pošljemo s `push`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">
</span>

![initial](slike/git/initial.png)

<span class="command">&lt;- push &lt;-</span>

![commit](slike/git/commit.png) ] Spremembe na strežnik pošljemo s `push`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">
</span>

![commit](slike/git/commit.png)

<span class="command">&lt;- push &lt;-</span>

![commit](slike/git/commit.png) ] Spremembe s strežnika povlečemo s `pull`

.center.git[ ![initial](slike/git/initial.png)

<span class="command">&lt;- pull &lt;-</span>

![commit](slike/git/commit.png)

<span class="command">
</span>

![commit](slike/git/commit.png) ] Spremembe s strežnika povlečemo s `pull`

.center.git[ ![commit](slike/git/commit.png)

<span class="command">&lt;- pull &lt;-</span>

![commit](slike/git/commit.png)

<span class="command">
</span>

![commit](slike/git/commit.png) ]

## Konflikti in zlivanje

Recimo, da na dveh koncih naredimo različni spremembi

.center.git[ ![commit](slike/git/commit.png)

<span class="command">
</span>

![commit](slike/git/commit.png)

<span class="command">commit =&gt;</span>

![commit](slike/git/commit.png) ] Recimo, da na dveh koncih naredimo različni spremembi

.center.git[ ![commit](slike/git/commit.png)

<span class="command">
</span>

![commit](slike/git/commit.png)

<span class="command">commit =&gt;</span>

![commit](slike/git/div-b.png) ] Recimo, da na dveh koncih naredimo različni spremembi

.center.git[ ![commit](slike/git/commit.png)

<span class="command">&lt;= commit</span>

![commit](slike/git/commit.png)

<span class="command">
</span>

![commit](slike/git/div-b.png) ] Recimo, da na dveh koncih naredimo različni spremembi

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">&lt;= commit</span>

![commit](slike/git/commit.png)

<span class="command">
</span>

![commit](slike/git/div-b.png) ] Kdor prvi pride, lahko naredi `push`

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">-&gt; push -&gt;</span>

![commit](slike/git/commit.png)

<span class="command">
</span>

![commit](slike/git/div-b.png) ] Kdor prvi pride, lahko naredi `push`

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">-&gt; push -&gt;</span>

![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/div-b.png) ] Drugega ukaza `push` strežnik **noče sprejeti**

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/div-a.png)

<span class="command">&lt;- push &lt;-</span>

![commit](slike/git/div-b.png) ] Drugega ukaza `push` strežnik **noče sprejeti**

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/div-a.png)

<span class="command" style="color: red">&lt;- push &lt;-</span>

![commit](slike/git/div-b.png) ] Z ukazom `pull` s strežnika poberemo in zlijemo spremembe

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/div-a.png)

<span class="command">-&gt; pull -&gt;</span>

![commit](slike/git/div-b.png) ] Z ukazom `pull` s strežnika poberemo in zlijemo spremembe

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/div-a.png)

<span class="command">-&gt; pull -&gt;</span>

![commit](slike/git/fetch.png) ] Z ukazom `pull` s strežnika poberemo in zlijemo spremembe

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/div-a.png)

<span class="command">merge =&gt;</span>

![commit](slike/git/merge.png) ] **Zlite** spremembe lahko nato pošljemo na strežnik

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/div-a.png)

<span class="command">&lt;- push &lt;-</span>

![commit](slike/git/merge.png) ] **Zlite** spremembe lahko nato pošljemo na strežnik

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">
</span>

![commit](slike/git/merge.png)

<span class="command">&lt;- push &lt;-</span>

![commit](slike/git/merge.png) ] **Zlite** spremembe lahko nato pošljemo na strežnik

.center.git[ ![commit](slike/git/div-a.png)

<span class="command">&lt;- pull &lt;-</span>

![commit](slike/git/merge.png)

<span class="command">
</span>

![commit](slike/git/merge.png) ] **Zlite** spremembe lahko nato pošljemo na strežnik

.center.git[ ![commit](slike/git/merge.png)

<span class="command">&lt;- pull &lt;-</span>

![commit](slike/git/merge.png)

<span class="command">
</span>

![commit](slike/git/merge.png) ]

## `README.md` in `.gitignore`

```
# Naslov
## Podnaslov

To je **debelo besedilo**. In zdaj sledi
naštevanje:

- beseda, lahko tudi `Pythonova`
- *ležeča besedna zveza*
- [FMF](http://www.fmf.uni-lj.si/)
```

--------------------------------------------------------------------------------

.tiny[# Naslov

## Podnaslov

To je **debelo besedilo**. In zdaj sledi naštevanje:

- beseda, lahko tudi `Pythonova`
- _ležeča besedna zveza_
- [FMF](http://www.fmf.uni-lj.si/) ]
