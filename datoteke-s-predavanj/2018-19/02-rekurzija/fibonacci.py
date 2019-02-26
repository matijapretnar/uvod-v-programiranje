# F0  F1  F2  F3  F4  F5  F6  F7
#  0   1   1   2   3   5   8  13

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(7)
