a, b, c = 4, 13, 15
s1 = (a + b + c) / 2
ploscina1 = (s1 * (s1 - a) * (s1 - b) * (s1 - c)) ** (1 / 2)

e, f = 3, 5
s2 = (a + e + f) / 2
ploscina2 = (s2 * (s2 - a) * (s2 - e) * (s1 - f)) ** (1 / 2)

ploscina = ploscina1 + ploscina2
