def f(x, y, *args, a=10, b=20, **kwargs):
    return (x, y, args, a, b, kwargs)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


class IteratorFibonaccijevih:
    def __init__(self):
        self.a, self.b = 0, 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.b - self.a  # da vrnemo prejšnjo vrednost a