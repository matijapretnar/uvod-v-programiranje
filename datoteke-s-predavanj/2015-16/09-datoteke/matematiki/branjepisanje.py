import os

print(os.getcwd())

with open('../klasiki/hlapec-jernej.txt') as f:
    stevec = 0
    with open('../klasiki/skriti-pomen-hlapca-jerneja.txt', 'w') as g:
        for vrstica in f:
            if stevec % 3 == 0:
                g.write(vrstica)
            stevec += 1



with open('../klasiki/gorjanci.txt', encoding='cp1250') as f:
    stevec = 0
    with open('../klasiki/skriti-pomen-gorjancev.txt', 'w', encoding='cp1250') as g:
        for vrstica in f:
            if stevec % 3 == 0:
                g.write(vrstica)
            stevec += 1
