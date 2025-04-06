def recherche(elt, tab):
    elt_index = None
    for i, x in enumerate(tab):
        if x == elt:
            elt_index = i
            break

    return elt_index

print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))