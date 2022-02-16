def fakulteta(n):
    """Vrne n! = n (n - 1) ... 2 1"""
    # Ker je n! = n (n - 1) ... 2 1 = n (n - 1)!
    # lahko funkcijo prevedemo na samo sebe
    # (taki funkciji pravimo rekurzivna)
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)
