with open('hlapec-jernej.txt') as f:
    urejene_vrstice = sorted(f)
with open('urejeni-hlapec-jernej.txt', 'w') as f:
    for vrstica in urejene_vrstice:
        f.write(vrstica)


