def recherche(tab, n):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if n == tab[m]:
            return m
        elif n > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return None

print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))