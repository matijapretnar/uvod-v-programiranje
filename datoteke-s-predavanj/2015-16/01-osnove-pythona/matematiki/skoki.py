k_tocka = 200
dolzina = 249.0
slog_a = 15
slog_b = 12.5
slog_c = 14
slog_d = 13.5
slog_e = 11
izravnava = 6.4

slog_min = min(slog_a, slog_b, slog_c, slog_d, slog_e)
slog_max = max(slog_a, slog_b, slog_c, slog_d, slog_e)
tocke_za_slog = slog_a + slog_b + slog_c + slog_d + slog_e - slog_min - slog_max

# točke za dolžino se pri letalnici (večje od 180 metrov) štejejo drugače
if k_tocka >= 180:
    osnovne_tocke = 120
    vrednost_metra = 1.2
else:
    osnovne_tocke = 60
    vrednost_metra = 1.8
tocke_za_dolzino = osnovne_tocke + vrednost_metra * (dolzina - k_tocka)

skupne_tocke = tocke_za_slog + tocke_za_dolzino + izravnava


def tocke_za_dolzino(dolzina, k_tocka):
    if k_tocka >= 180:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    else:
        osnovne_tocke = 60
        vrednost_metra = 1.8
    return osnovne_tocke + vrednost_metra * (dolzina - k_tocka)
