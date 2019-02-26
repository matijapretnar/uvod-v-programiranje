import math

a = 4
b = 13
c = 15

# Ploščino bomo izračunali s pomočjo Heronovega obrazca
s = (a + b + c) / 2
ploscina1 = math.sqrt(s * (s - a) * (s - b) * (s - c))
ploscina2 = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
