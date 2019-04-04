import os
import random


def permutiraj(permutacija, moznosti):
    return [moznosti[i] for i in permutacija]

def nakljucna_permutacija(n):
    return random.sample(range(n), n)

def nastej_odgovore(odgovori):
    niz = '\\begin{enumerate}[(a)]\n'
    for odgovor in odgovori:
        niz += '\\item {}\n'.format(odgovor)
    niz += '\\end{enumerate}\n'
    return niz

def pomesaj_odgovore(pravilen_odgovor, napacni_odgovori):
    vsi_odgovori = [pravilen_odgovor] + napacni_odgovori
    permutacija = nakljucna_permutacija(len(vsi_odgovori))
    odgovori = permutiraj(permutacija, vsi_odgovori)
    resitev = chr(ord('a') + permutacija.index(0))
    return odgovori, resitev 

def izloci_besedilo_in_pomesaj_odgovore(vprasanja_z_odgovori):
    permutacija = nakljucna_permutacija(len(vprasanja_z_odgovori))
    vprasanja_z_odgovori = permutiraj(permutacija, vprasanja_z_odgovori)
    vprasanja, odgovori = zip(*vprasanja_z_odgovori)
    pravilen_odgovor = random.randrange(len(odgovori))
    vprasanje = vprasanja[permutacija.index(pravilen_odgovor)]
    resitev = chr(ord('a') + permutacija.index(pravilen_odgovor))
    return vprasanje, odgovori, resitev 

def pomesaj_vrstni_red(pravilen_vrstni_red):
    permutacija = nakljucna_permutacija(len(pravilen_vrstni_red))
    odgovori = permutiraj(permutacija, pravilen_vrstni_red)
    resitev = ''.join(str(i) for i in permutacija)
    return odgovori, resitev 


def kateri_program_nastavi_vrednosti():
    a, b, c = random.choice(['abc', 'xyz', 'kmn', 'uvw'])
    x, y = random.sample(range(1, 10), 2)
    besedilo = fr'''
        Kateri izmed programov pri začetnem stanju
            \inlinepy{{{a} = {x}}} in
            \inlinepy{{{b} = {y}}}
        nastavi vrednosti
            \inlinepy{{{a} = {y}}},
            \inlinepy{{{b} = {x}}} in
            \inlinepy{{{c} = {x + y}}}?
    '''
    odgovori, resitev = pomesaj_odgovore(
        fr'''
            \begin{{minted}}[autogobble]{{python}}
            {c} = {a}
            {a} = {b}
            {b} = {c}
            {c} = {a} + {b}
            \end{{minted}}
        ''', [
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                {a} = {b}
                {c} = {b}
                {b} = {a}
                {c} = {a} + {b}
                \end{{minted}}
            ''', 
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                {c} = {a}
                {b} = {c}
                {a} = {b}
                {c} = {a} + {b}
                \end{{minted}}
            ''',
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                {a} = {b}
                {b} = {c}
                {c} = {a}
                {c} = {a} + {b}
                \end{{minted}}
            ''',            
        ]
    )
    naloga = fr'''
        \naloga*
        {besedilo}
        \begin{{multicols}}{{4}}
        {nastej_odgovore(odgovori)}
        \end{{multicols}}
    '''
    return naloga, resitev


def kaksne_vrste_napak():
    vprasanje, odgovori, resitev = izloci_besedilo_in_pomesaj_odgovore([
        (fr"""
            define fibonacci(n):
                if n <= 0:
                    return 0
                elif n == 1
                    return 1
                else:
                    a = fibonacci(n - 1)
                    b = fibonacci(n - 2)
                  return a + b
            """,
            'sintaktične napake, zaradi katerih Python programa noče izvesti.'
        ),
        (fr"""
            def fibonacci(n):
                if n <= 0:
                    return 0
                elif n == 1:
                    return 1
                else:
                    a = fibonacci(n - '1')
                    b = fib(n - 2)
                    return a + b
            """,
            'napake, zaradi katerih Python prekine z izvajanjem programa'
        ),
        (fr"""
            def fibonacci(n):
                if n <= 0:
                    return 0
                elif n == 1:
                    return 0
                else:
                    a = fibonacci(n - 1)
                    b = fibonacci(n - 3)
                    return a * b
            """,
            'vsebinske napake, zaradi katerih Python izračuna napačen rezultat'
        ),
        (fr"""
            def fibonacci(n):
                if n<=0:
                    return (0)
                elif n==1:
                    return (1)
                else:
                    a = fibonacci(n - 1)
                    b = fibonacci(n - 2)
                    return   a + b
            """,
            'oblikovne napake, ki ne vplivajo na pravilnost rezultata'
        ),
    ])

    naloga = fr'''
        \naloga*
        \begin{{multicols}}{{2}}
        \noindent
        Kakšne vrste napak vsebuje program na desni?

        {nastej_odgovore(odgovori)}
        \columnbreak

        \begin{{minted}}[baselinestretch=1.2,escapeinside=||, autogobble]{{python}}
        {vprasanje}
        \end{{minted}}

        \end{{multicols}}

    '''
    return naloga, resitev


def kaj_izracuna_funkcija():
    x = random.choice(['x', 'z', 'znak'])
    niz = random.choice(['niz', 'besedilo', 'stavek'])
    vprasanje, odgovori, resitev = izloci_besedilo_in_pomesaj_odgovore([
        (fr'''
            def f({niz}):
                for {x} in {niz}:
                    if {x} in 'aeiouAEIOU':
                        return True
                return False
            ''',
            'ali niz vsebuje kakšen samoglasnik'
        ),
        (fr'''
            def f({niz}):
                for {x} in {niz}:
                    if {x} not in 'aeiouAEIOU':
                        return False
                return True
            ''',
            'ali niz vsebuje samo samoglasnike'
        ),
        (fr'''
            def f({niz}):
                for {x} in {niz}:
                    if {x} in 'aeiouAEIOU':
                        return False
                return True
            ''',
            'ali niz ne vsebuje nobenega samoglasnika'
        ),
        (fr'''
            def f({niz}):
                for {x} in {niz}:
                    if {x} not in 'aeiouAEIOU':
                        return True
                return False
            ''',
            'ali niz vsebuje znak, ki ni samoglasnik'
        ),
    ])

    naloga = fr'''
        \naloga*

        \begin{{multicols}}{{2}}
        \noindent
        Kateri pogoj preverja spodnja funkcija?
        \begin{{minted}}[autogobble]{{python}}
        {vprasanje}
        \end{{minted}}

        {nastej_odgovore(odgovori)}
        \end{{multicols}}
    '''
    return naloga, resitev



def kaj_izpise_program():
    f, g, x, y = random.choice([
        ('f', 'g', 'x', 'y'),
        ('f', 'g', 'a', 'b'),
        ('a', 'b', 'x', 'y'),
        ('p', 'q', 'a', 'b'),
    ])
    a, b, c = random.sample(range(1, 10), 3)
    vprasanje, odgovori, resitev = izloci_besedilo_in_pomesaj_odgovore([
        (fr'''
            def {f}({x}):
                print({x})
                return {x} + {a}

            def {g}({y}):
                print({y})
                return {b} * {y}
        ''',
        fr'''\inlinepy{{{[c, b * c, b * c + a]}}}'''
        ),
        (fr'''
            def {f}({x}):
                print({x})
                return {x} + {a}

            def {g}({y}):
                return {b} * {y}
                print({y})
        ''',
        fr'''\inlinepy{{{[b * c, b * c + a]}}}'''
        ),
        (fr'''
            def {f}({x}):
                return {x} + {a}
                print({x})

            def {g}({y}):
                print({y})
                return {b} * {y}
        ''',
        fr'''\inlinepy{{{[c, b * c + a]}}}'''
        ),
        (fr'''
            def {f}({x}):
                return {x} + {a}
                print({x})

            def {g}({y}):
                return {b} * {y}
                print({y})
        ''',
        fr'''\inlinepy{{{[b * c + a]}}}'''
        ),
    ])

    naloga = fr'''
        \naloga*
        Katere vrstice izpiše klic \inlinepy{{print({f}({g}({c})))}}, če sta funkciji \inlinepy{{{f}}} in \inlinepy{{{g}}} definirani kot spodaj?

        \begin{{multicols}}{{2}}
        \begin{{minted}}[autogobble]{{python}}
        {vprasanje}
        \end{{minted}}

        {nastej_odgovore(odgovori)}
        \end{{multicols}}
    '''
    return naloga, resitev


def katera_funkcija_izracuna_ostanek():
    m, n = random.choice([('a', 'b'), ('x', 'y'), ('m', 'n'), ('u', 'v')])
    besedilo = fr'''
        Katera izmed spodnjih funkcij izračuna ostanek pri deljenju naravnega števila \inlinepy{{{m}}} z naravnim številom \inlinepy{{{n}}}?
    '''
    odgovori, resitev = pomesaj_odgovore(
        fr'''
            \begin{{minted}}[autogobble]{{python}}
            def ostanek({m}, {n}):
                if {m} < {n}:
                    return {m}
                else:
                    return ostanek({m} - {n}, {n})
            \end{{minted}}
        ''', [
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                def ostanek({m}, {n}):
                    if {m} < {n}:
                        return {m}
                    else:
                        return ostanek({m} % {n})
                \end{{minted}}
            ''',
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                def ostanek({m}, {n}):
                    if {m} < {n}:
                        return 0
                    else:
                        return ostanek({m} - {n}, {n})
                \end{{minted}}
            ''',
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                def ostanek({m}, {n}):
                    if {n} == 0:
                        return {m}
                    else:
                        return ostanek({n}, {m} % {n})
                \end{{minted}}
            '''
        ]
    )
    naloga = fr'''
        \clearpage
        \naloga
        {besedilo}
        \begin{{multicols}}{{2}}
        {nastej_odgovore(odgovori)}
        \end{{multicols}}
    '''
    return naloga, resitev


def drugacen_izpis_kot_ostale():
    i = random.choice('ijxn')
    m = random.choice([10, 20, 50])
    n = random.choice([2, 3, 5])
    besedilo = fr'''
        Kateri izmed spodnjih programov ima drugačen izpis kot ostali?
    '''
    odgovori, resitev = pomesaj_odgovore(
        fr'''
            \begin{{minted}}[autogobble]{{python}}
                for {i} in range(1, {m}):
                    if {i} % {n} != 0:
                        continue
                    print({i})
            \end{{minted}}
        ''', [
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                    for {i} in range(1, {m * n}, {n}):
                        if {i} > {m}:
                            break
                        print({i})
                \end{{minted}}
            ''', 
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                    for {i} in range(1, {m * n}, {n}):
                        if {i} < {m}:
                            print({i})
                \end{{minted}}
            ''',
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                    for {i} in range(1, {m}):
                        if {i} % {n} == 1:
                            print({i})
                        continue
                \end{{minted}}
            ''',            
        ]
    )
    naloga = fr'''
        \naloga*
        {besedilo}
        \begin{{multicols}}{{2}}
        {nastej_odgovore(odgovori)}
        \end{{multicols}}
    '''
    return naloga, resitev

def drugacen_rezultat():
    f = random.choice('fgh')
    xyz = random.choice([('x', 'y', 'z'), ('p', 'q', 'r'), ('a', 'b', 'c')])
    x, y, z = random.sample(xyz, 3)
    besedilo = fr'''
        Katera izmed funkcij vrača drugačne rezultate kot ostale?
    '''
    odgovori, resitev = pomesaj_odgovore(
        fr'''
            \begin{{minted}}[autogobble]{{python}}
            def {f}({x}, {y}, {z}):
                if not {z}:
                    return {x} and {y}
                else:
                    return False
            \end{{minted}}
        ''', [
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                def {f}({x}, {y}, {z}):
                    if {x}:
                        return {y} and {z}
                    else:
                        return False
                \end{{minted}}
            ''', 
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                def {f}({x}, {y}, {z}):
                    if {x} and {y}:
                        return {z}
                    else:
                        return False
                \end{{minted}}
            ''',
            fr'''
                \begin{{minted}}[autogobble]{{python}}
                def {f}({x}, {y}, {z}):
                    if not {y}:
                        return False
                    else:
                        return {x} and {z}
                \end{{minted}}
            ''',            
        ]
    )
    naloga = fr'''
        \naloga*
        {besedilo}
        \begin{{multicols}}{{2}}
        {nastej_odgovore(odgovori)}
        \end{{multicols}}
    '''
    return naloga, resitev



def dopolni_program():
    x, y = random.choice([('x', 'y'), ('a', 'b'), ('p', 'q')])
    vsota = random.choice([True, False])
    prvi = random.choice([True, False])
    if not prvi:
        x, y = y, x
    acc = 'vs' if vsota else 'zm'
    
    naloga = fr'''
        \naloga*
        \begin{{multicols}}{{2}}
        \noindent
        V vsak prostor vpišite \textbf{{natanko en znak}} tako, da bo dobljeni program v spremenljivko \inlinepy{{{acc}}} shranil {'vsoto' if vsota else 'zmnožek'} števil \inlinepy{{{x}}} in \inlinepy{{{y}}}:
        
        \columnbreak
        \begin{{minted}}[baselinestretch=1.2,escapeinside=||]{{python}}
        {acc} = |\answerbox{{0.5}}|
        while {x} > |\answerbox{{0.5}}|:
            {acc} += |\answerbox{{0.5}}|
            |\answerbox{{0.5}}| -= 1
        \end{{minted}}
        \end{{multicols}}
    '''
    resitev = fr'''\inlinepy{{{y if vsota else 0}0{1 if vsota else y}{x}}}'''
    return naloga, resitev


def napisite_katerikoli_stevili():
    sodo = random.choice([True, False])
    nizi = random.choice([True, False])
    f = random.choice('fgh')
    i = random.choice('ij')
    if nizi:
        x, y = random.choice([('str1', 'str2'), ('niz1', 'niz2')])
    else:
        x, y = random.choice([('sez1', 'sez2'), ('lst1', 'lst2')])
    
    naloga = fr'''
        \naloga*
        \begin{{multicols}}{{2}}
        \noindent
        Napišite primer vrednosti spremenljivk \inlinepy{{{x}}} in \inlinepy{{{y}}}, za kateri klic \inlinepy{{{f}({x}, {y})}} vrne \inlinepy{{True}}.
        \begin{{minted}}[baselinestretch=1.2, escapeinside=||]{{python}}
        {x} = |\answerbox{{3}}|
        {y} = |\answerbox{{3}}|
        \end{{minted}}
        \vfil
        \columnbreak
        \begin{{minted}}[autogobble]{{python}}
        def {f}({x}, {y}):
            if len({x}) != len({y}) or len({x}) < 3:
                return False
            for {i} in range(len({x})):
                if {i} % 2 == {0 if sodo else 1} and {x}[{i}] != {y}[{i}]:
                    return False
            return True
        \end{{minted}}
        \end{{multicols}}
    '''
    resitev = fr'''
        \inlinepy{{{x}}} in \inlinepy{{{y}}} dolžine vsaj 3, ki se ujemata na {'sodih' if sodo else 'lihih'} mestih
    '''
    return naloga, resitev


def oznaci_vrstni_red():
    sez1, sez2 = random.choice([('sez1', 'sez2'), ('lst1', 'lst2'), ('sez2', 'sez1'), ('lst2', 'lst1')])
    x, y, z = random.sample(range(1, 10), 3)
    besedilo = fr'''
        S številkami od $0$ do $4$ označite vrstni red, v katerem moramo izvesti ukaze na desni, da bo na koncu spremenljivka \inlinepy{{{sez2}}} kazala na seznam \inlinepy{{{[x, y, z]}}}?
    '''
    odgovori, resitev = pomesaj_vrstni_red([
        f'''|\\answerbox{{0.5}}| {sez1} = [{y}]\n''',
        f'''|\\answerbox{{0.5}}| {sez2} = {sez1}\n''',
        f'''|\\answerbox{{0.5}}| {sez1} = [{x}]\n''',
        f'''|\\answerbox{{0.5}}| {sez2}.append({z})\n''',
        f'''|\\answerbox{{0.5}}| {sez2} = {sez1} + {sez2}\n''',
    ])
    naloga = fr'''
        \naloga*
        \begin{{multicols}}{{2}}
        \noindent {besedilo}
        \columnbreak
        \noindent
        \begin{{minted}}[baselinestretch=1.2, escapeinside=||]{{python}}
{''.join(odgovori)}
        \end{{minted}}
        \end{{multicols}}
    '''
    return naloga, resitev


def ustvari_izpite(stevilo_izpitov, naloge):
    izpiti = []
    for st_izpita in range(stevilo_izpitov):
        navodila = []
        resitve = []
        for st_naloge, naloga in enumerate(naloge):
            random.seed((st_izpita, st_naloge))
            navodilo, resitev = naloga()
            navodila.append(navodilo)
            resitve.append(resitev)
        izpiti.append((navodila, resitve))
    return izpiti


def zapisi_datoteke(izpiti, datoteka_z_navodili, datoteka_z_resitvami):
    glava = r'''
        \documentclass[arhiv, 10pt]{../izpit}
        \usepackage{fouriernc}
        \usepackage{minted}
        \usepackage{booktabs}
        \usepackage{multicol}
        \usepackage{paralist}
        \usepackage{inconsolata}
        \usepackage[T1]{fontenc}
        \usepackage{xcolor}
        \usepackage[most]{tcolorbox}

        \definecolor{light-red}{rgb}{1,0.5,0.5}
        \usemintedstyle{colorful}
        \setlength{\columnsep}{30pt}
        \setlength{\textheight}{1.1\textheight}
        \tcbset{enhanced jigsaw,size=tight,colback=light-red,boxrule=0pt,extrude by=1pt,rounded corners,interior style={opacity=0.3}}
        \newcommand{\inlinepy}[1]{\mintinline{python}{#1}}
        \newcommand{\answerbox}[1]{\framebox{\vphantom{\large M}\hspace{#1cm}}}
        \newcommand{\wrongbox}[1]{\tcbox{\vphantom{M}#1}}
    '''
    with open(datoteka_z_navodili, 'w') as datoteka:
        datoteka.write(glava)
        datoteka.write(r'''\begin{document}''')
        for i, (navodila, _) in enumerate(izpiti, 1):
            datoteka.write(fr'''
            \izpit[ucilnica=205, naloge=-1]{{Uvod v programiranje: Kolokvij \#{i:03}}}{{27.\ marec 2019}}{{
                Pri vsaki nalogi obkrožite črko pred pravilnim odgovorom ali vpišite pravilno vrednost v ustrezen prostor. \\
                Čas reševanja je 30 minut. Veliko uspeha!
            }}
            ''')
            for navodilo in navodila:
                datoteka.write(navodilo)
        datoteka.write(r'''\end{document}''')
    with open(datoteka_z_resitvami, 'w') as datoteka:
        datoteka.write(glava)
        datoteka.write(r'''
            \begin{document}
            \makebox[\textwidth][c]{\begin{tabular}{rcccccccccc} \toprule
            \textbf{Kolokvij} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\ \midrule
        ''')
        for i, (_, resitve) in enumerate(izpiti, 1):
            datoteka.write('\\textbf{{\\#{:03}}} & {}\\\\\n'.format(i, ' & '.join(resitve)))
        datoteka.write(r'''
            \bottomrule
            \end{tabular}}
            \end{document}
        ''')


os.chdir(os.path.dirname(__file__))
izpiti = ustvari_izpite(50, [
    kateri_program_nastavi_vrednosti,
    kaksne_vrste_napak,
    kaj_izpise_program,
    kaj_izracuna_funkcija,
    dopolni_program,
    katera_funkcija_izracuna_ostanek,
    drugacen_rezultat,
    drugacen_izpis_kot_ostale,
    napisite_katerikoli_stevili,
    oznaci_vrstni_red,
])
zapisi_datoteke(izpiti, 'naloge.tex', 'resitve.tex')
