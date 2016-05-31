class Fibonacci:
    def __init__(self):
        self.zdaj = 0
        self.potem = 1

    def __next__(self):
        povedal_bom = self.zdaj
        self.zdaj, self.potem = self.potem, self.zdaj + self.potem
        return povedal_bom

    def __iter__(self):
        return self





for x in 'abcd':
    print(2 * x)


iterator_po_abcd = iter('abcd')
while True:
    try:
        x = next(iterator_po_abcd)
    except StopIteration:
        break
    print(2 * x)


for f in Fibonacci():
    print(f)
