def tri_selection(tab):
    n = len(tab)
    for i in range(n):
        min = tab[i]
        indice_min = i
        for j in range(i, n):
            if min > tab[j]:
                min = tab[j]
                indice_min = j
        tab[indice_min] = tab[i]
        tab[i] = min

tab = [1, 52, 6,-9, 12]
tri_selection(tab)
print(tab)
