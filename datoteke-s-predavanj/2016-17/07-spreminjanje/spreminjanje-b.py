def stevilo_sodih_elementov(seznam):
    stevilo = 0
    for element in seznam:
        if element % 2 == 0:
            stevilo += 1
    return stevilo

def podseznam_sodih_elementov(seznam):
    podseznam = []
    for element in seznam:
        if element % 2 == 0:
            podseznam.append(element)
    return podseznam

def podseznam_kvadratov_sodih_elementov(seznam):
    podseznam = []
    for element in seznam:
        if element % 2 == 0:
            podseznam.append(element ** 2)
    return podseznam

def podseznam_kvadratov_sodih_elementov(seznam):
    return [x ** 2 for x in seznam if x % 2 == 0]

def seznam_delnih_vsot(seznam):
    delne_vsote = [seznam[0]]
    for i in range(1, len(seznam)):
        delne_vsote.append(seznam[i] + delne_vsote[-1])
    return delne_vsote

print(stevilo_sodih_elementov([10, 2, 5, 6]))
print(podseznam_sodih_elementov([10, 2, 5, 6]))
print(podseznam_kvadratov_sodih_elementov([10, 2, 5, 6]))
print(seznam_delnih_vsot([10, 2, 5, 6]))