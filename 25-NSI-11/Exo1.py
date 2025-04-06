def parcours_largeur(abr):
    l = []
    f = [abr]
    while f:
        a = f.pop(0)
        if a is None:
            continue
        f.append(a[0])
        f.append(a[2])
        l.append(a[1])

    return l

arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )
print(parcours_largeur(arbre))