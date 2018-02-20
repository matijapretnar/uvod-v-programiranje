import math

a, b, c = 3, 4, 5
# Uporabili bomo Heronov obrazec
# (https://sl.wikipedia.org/wiki/Heronova_formula)
s = (a + b + c) / 2
p = math.sqrt(s * (s - a) * (s - b) * (s - c))


a, b, c, d, e, f = 18, 21, 22, 25, 27, 31
s_abc = (a + b + c) / 2
p_abc = math.sqrt(s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c))
s_aef = (a + e + f) / 2
p_aef = math.sqrt(s_aef * (s_aef - a) * (s_aef - e) * (s_aef - f))
s_bef = (b + e + f) / 2
p_bef = math.sqrt(s_bef * (s_bef - b) * (s_bef - e) * (s_bef - f))
s_cdf = (c + d + f) / 2
p_cdf = math.sqrt(s_cdf * (s_cdf - c) * (s_cdf - d) * (s_cdf - f))
povrsina = p_abc + p_ade + p_bef + p_cdf
