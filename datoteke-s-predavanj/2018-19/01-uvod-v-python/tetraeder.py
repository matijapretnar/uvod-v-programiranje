a = 18
b = 21
c = 22
d = 25
e = 27
f = 31

s_abc = (a + b + c) / 2
s_aef = (a + e + f) / 2
s_bdf = (b + d + f) / 2
s_cde = (c + d + e) / 2
p_abc = (s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c)) ** (1 / 2)
p_aef = (s_aef * (s_aef - a) * (s_aef - e) * (s_aef - f)) ** (1 / 2)
p_bdf = (s_bdf * (s_bdf - b) * (s_bdf - d) * (s_bdf - f)) ** (1 / 2)
p_cde = (s_cde * (s_cde - c) * (s_cde - d) * (s_cde - e)) ** (1 / 2)
