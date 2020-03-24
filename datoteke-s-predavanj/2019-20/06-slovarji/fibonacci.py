ze_izracunani = {}

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in ze_izracunani:
        return ze_izracunani[n]
    else:
        print(n)
        fib_n = fibonacci(n - 1) + fibonacci(n - 2)
        ze_izracunani[n] = fib_n
        return fib_n
