from collections import defaultdict
import random

def preberi_nepovezane_besede(besedilo):
    return set(besedilo.split())

def nepovezane_besede(izvirnik, dolzina=200):
    stare_besede = preberi_nepovezane_besede(izvirnik)
    nove_besede = random.sample(stare_besede, dolzina)
    return ' '.join(nove_besede)

def preberi_povezave_med_besedami(besedilo):
    besede = besedilo.split()
    naslednje_besede = defaultdict(list)
    for i in range(len(besede) - 1):
        prva, druga = besede[i], besede[i + 1]
        naslednje_besede[prva].append(druga)
    return naslednje_besede

def povezane_besede(izvirnik, dolzina=200):
    naslednje_besede = preberi_povezave_med_besedami(izvirnik)
    prva_beseda = izvirnik.split()[0]
    nove_besede = [prva_beseda]
    for _ in range(dolzina):
        nove_besede.append(random.choice(naslednje_besede[nove_besede[-1]]))
    return ' '.join(nove_besede)

with open('datoteke-s-predavanj/2019-20/07-datoteke/martin-krpan.txt') as datoteka:
    vsebina = datoteka.read()
    nov_martin_krpan = povezane_besede(vsebina)
    print(nov_martin_krpan)
