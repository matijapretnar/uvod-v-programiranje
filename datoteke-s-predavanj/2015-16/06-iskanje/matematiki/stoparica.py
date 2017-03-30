import timeit
import matplotlib.pyplot as plt
import iskanje

POLOZAJ = 0.5
VELIKOST = 10 ** 4
SEZNAM = list(range(10 * VELIKOST))


def izmeri(algo, ime_algoritma, dolzine, polozaj):
    """
    Vrni seznam časov, ki jih algoritem potrebuje za urejanje seznamov dolzin dolzine.
    """
    casi = []
    for dolzina in dolzine:
        seznam = SEZNAM[:dolzina]
        x = round(dolzina * polozaj)
        casi.append(timeit.timeit(lambda: algo(seznam, x), number=10))
    return casi

dolzine = list(range(VELIKOST, 10 * VELIKOST + 1, VELIKOST))
t1 = izmeri(iskanje.poisci_v_neurejenem, 'Iskanje v neurejenem', dolzine, POLOZAJ)
plt.plot(dolzine, t1, 'r')
t2 = izmeri(iskanje.poisci_v_urejenem_napacen, 'Napačno iskanje v urejenem', dolzine, POLOZAJ)
plt.plot(dolzine, t2, 'b')
t3 = izmeri(iskanje.poisci_v_urejenem, 'Iskanje v urejenem', dolzine, POLOZAJ)
plt.plot(dolzine, t3, 'g')

plt.show()
