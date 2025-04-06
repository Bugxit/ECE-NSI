def recherche_indices_classement(elt, tab):
    res = ([], [], [])
    for i, x in enumerate(tab):
        if x < elt:
            res[0].append(i)
        elif x > elt:
            res[2].append(i)
        else:
            res[1].append(i)

    return res

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print(recherche_indices_classement(3, []))
