def fibonacci():
    zdaj, potem = 0, 1
    while True:
        yield zdaj
        zdaj, potem = potem, zdaj + potem

def enostavni_generator(n):
    yield n + 1
    yield n + 2
    yield 10 * n
