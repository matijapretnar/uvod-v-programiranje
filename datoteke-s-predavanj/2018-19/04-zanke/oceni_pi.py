import random

stevilo_vseh_tock = 1000000
stevilo_tock_v_krogu = 0
for st_poskusa in range(stevilo_vseh_tock):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        stevilo_tock_v_krogu += 1
print('pi je približno', 4 * stevilo_tock_v_krogu / stevilo_vseh_tock)

import math

stevilo_vseh_tock = 1000000
stevilo_tock_pod_grafom = 0
for st_poskusa in range(stevilo_vseh_tock):
    x = random.random()
    y = random.random()
    if y <= math.sin(x):
        stevilo_tock_pod_grafom += 1
print('integral sin(x) od 0 do 1 je približno', stevilo_tock_pod_grafom / stevilo_vseh_tock)

