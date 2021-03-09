import random

ST_TOCK = 2
st_tock_v_krogu = 0

for _ in range(ST_TOCK):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        st_tock_v_krogu += 1
print(f"pi je približno {4 * st_tock_v_krogu / ST_TOCK}")
