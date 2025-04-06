def voisins_entrants(adj, x):
    liste_v_e = []
    for i, e in enumerate(adj):
        if x in e:
            liste_v_e.append(i)

    return liste_v_e


print(voisins_entrants([[1, 2], [2], [0], [0]], 0))
print(voisins_entrants([[1, 2], [2], [0], [0]], 1))