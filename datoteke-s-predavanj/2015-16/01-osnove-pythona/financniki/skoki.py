dolzina = 249.0
slog_a = 15
slog_b = 12.5
slog_c = 14
slog_d = 13.5
slog_e = 11
izravnava = 6.4

k_tocka = 200
letalnica = k_tocka >= 185

if letalnica:
    osnovne_tocke = 120
    vrednost_metra = 1.2
else:
    osnovne_tocke = 60
    vrednost_metra = 1.8

tocke_dolzina = osnovne_tocke + vrednost_metra * (dolzina - k_tocka)

slog_min = min(slog_a, slog_b, slog_c, slog_d, slog_e)
slog_max = max(slog_a, slog_b, slog_c, slog_d, slog_e)
tocke_slog = slog_a + slog_b + slog_c + slog_d + slog_e - slog_min - slog_max

skupne_tocke = tocke_dolzina + tocke_slog + izravnava