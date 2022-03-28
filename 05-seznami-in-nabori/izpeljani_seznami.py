def seznam_kvadratov(n):
    kvadrati = []
    for i in range(1, n + 1):
        kvadrati.append(i ** 2)
    return kvadrati

# { n² | n ∈ {1, ..., 10}}
# [n ** 2 for n in range(1, 11)]

def izpeljani_seznam_kvadratov(n):
    return [i ** 2 for i in range(1, n + 1)]

def seznam_sodih_kvadratov(n):
    return [i ** 2 for i in range(1, n + 1) if i % 2 == 0]
