def stopnja_dohodnine(letna_davcna_osnova):
    if letna_davcna_osnova < 8500:
        return 0.16 * letna_davcna_osnova
    elif letna_davcna_osnova < 25000:
        return 1360 + 0.26 * (letna_davcna_osnova - 8500)
    elif letna_davcna_osnova < 50000:
        return 5650 + 0.33 * (letna_davcna_osnova - 25000)
    elif letna_davcna_osnova < 72000:
        return 13900 + 0.39 * (letna_davcna_osnova - 50000)
    else:
        return 22480 + 0.50 * (letna_davcna_osnova - 72000)
