def odmera_dohodnine(letna_davcna_osnova):
    """Izračuna letni znesek dohodnine pri dani davčni osnovi."""
    if letna_davcna_osnova < 8500.00:
        return 0.16 * letna_davcna_osnova
    elif letna_davcna_osnova < 25000.00:
        return 1360.00 + 0.26 * (letna_davcna_osnova - 8500.00)
    elif letna_davcna_osnova < 50000.00:
        return 5650.00 + 0.33 * (letna_davcna_osnova - 25000.00)
    elif letna_davcna_osnova < 72000.00:
        return 13900.00 + 0.39 * (letna_davcna_osnova - 50000.00)
    else:
        return 22480.00 + 0.50 * (letna_davcna_osnova - 72000.00)

def splosna_olajsava(skupni_dohodek):
    """Izračuna splošno olajšavo pri skupnem letnem dohodku."""
    if skupni_dohodek <= 13316.83:
        return 3500.00 + (18700.38 - 1.40427 * skupni_dohodek)
    else:
        return 3500.00

def koliko_mi_ostane_na_mesec(mesecni_dohodek):
    """Izračuna, koliko mesečnega dohodka ostane po obračunu dohodnine."""
    letni_dohodek = 12 * mesecni_dohodek
    # Ker smo leni, program upošteva le splošno olajšavo,
    # ostalih osebnih in posebnih olajšav pa ne.
    olajsava = splosna_olajsava(letni_dohodek)
    davcna_osnova = max(letni_dohodek - olajsava, 0)
    dohodnina = odmera_dohodnine(davcna_osnova)
    letni_ostanek = letni_dohodek - dohodnina
    mesecni_ostanek = round(letni_ostanek / 12, 2)
    return mesecni_ostanek
