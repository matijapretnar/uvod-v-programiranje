def odmera_dohodnine(davcna_osnova):
    '''Izračuna letni znesek dohodnine pri dani davčni osnovi.'''
    if davcna_osnova <= 8021.34:
        return 0.16 * davcna_osnova
    elif davcna_osnova <= 20400.00:
        return 1283.41 + 0.27 * (davcna_osnova - 8021.34)
    elif davcna_osnova <= 48000.00:
        return 4625.64 + 0.34 * (davcna_osnova - 20400.00)
    elif davcna_osnova <= 70907.20:
        return 14009.65 + 0.39 * (davcna_osnova - 48000.00)
    else:
        return 22943.46 + 0.50 * (davcna_osnova - 70907.20)

def splosna_olajsava(skupni_dohodek):
    '''Izračuna splošno olajšavo pri skupnem letnem dohodku.'''
    if skupni_dohodek <= 11166.37:
        return 6519.82
    elif skupni_dohodek <= 13316.83:
        return 3302.70 + (19922.15 - 1.49601 * skupni_dohodek)
    else:
        return 3302.70

def koliko_mi_ostane_na_mesec(mesecni_dohodek):
    '''Izračuna, koliko mesečnega dohodka ostane po obračunu dohodnine.'''
    letni_dohodek = 12 * mesecni_dohodek
    # Ker smo leni, program upošteva le splošno olajšavo,
    # ostalih osebnih in posebnih olajšav pa ne.
    olajsava = splosna_olajsava(letni_dohodek)
    davcna_osnova = max(letni_dohodek - olajsava, 0)
    dohodnina = odmera_dohodnine(davcna_osnova)
    letni_ostanek = letni_dohodek - dohodnina
    mesecni_ostanek = round(letni_ostanek / 12, 2)
    return mesecni_ostanek

koliko_mi_ostane_na_mesec(300)

