def kvadrat(n):
    return n ** 2

def izpisi_kvadrat(n):
    print(n ** 2)

def niz_kvadrata(n):
    return str(n ** 2)

def izpisi_zvezdice(n):
    if n > 0:
        print(n * '*')
        izpisi_zvezdice(n - 1)

def izpisi_kvadrat(n):
    print("┌" + (n - 2) * '-' + "┐")
    izpisi_rob(n, n)
    print("└" + (n - 2) * '-' + "┘")

def izpisi_rob(visina, sirina):
    if visina > 0:
        print('|' + (sirina - 2) * ' ' + '|')
        izpisi_rob(visina - 1, sirina)

def lepo_se_pogovarjaj():
    print('Živjo, kako ti je ime?')
    ime = input()
    print(f'Me veseli, da sem te spoznal {ime}.')
    print('Zdaj pa moram žal iti. Se vidiva.')

def risi_kvadrate():
    print('Kako velik kvadrat bi rad narisal?')
    n = input()
    izpisi_kvadrat(int(n))
    risi_kvadrate()
