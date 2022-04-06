class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    
    def __next__(self):
        stari_a = self.a
        novi_b = self.a + self.b
        self.a = self.b
        self.b = novi_b
        if stari_a < 100:
            return stari_a
        else:
            raise StopIteration

def fibonacci():
    a = 0
    b = 1
    while True:
        if a < 100:
            yield a
        else:
            return
        a, b = b, a + b
