def fibonacci(n):
    """Vrne n-ti člen Fibonaccijevega zaporedja 0 1 1 2 3 5 8 13 21 ..."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_splosni(n, a=0, b=1):
    """Vrne n-ti člen Fibonaccijevega zaporedja a b a+b a+2b 2a+3b 3a+5b 5a+8b ..."""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_splosni(n - 1, b, a + b)
