import math

a = 4
b = 13
c = 15
s = (a + b + c) / 2
p = math.sqrt(s * (s - a) * (s - b) * (s - c))


a = 3
b = 3
c = 4
d = 5
e = 5
f = 6
s_abc = (a + b + c) / 2
p_abc = math.sqrt(s * (s_abc - a) * (s_abc - b) * (s_abc - c))
s = (a + d + e) / 2
p_ade = math.sqrt(s * (s - a) * (s - d) * (s - e))
s = (b + e + f) / 2
p_bef = math.sqrt(s * (s - b) * (s - e) * (s - f))
s = (c + d + f) / 2
p_cdf = math.sqrt(s * (s - c) * (s - d) * (s - f))
povrsina = p_abc + p_ade + p_bef + p_cdf
