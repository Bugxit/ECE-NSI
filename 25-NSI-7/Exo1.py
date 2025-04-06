def nbr_occurrences(chaine):
    dico = {}
    for c in chaine:
        if c not in dico:
            dico[c] = 1
        else:
            dico[c] += 1

    return dico

print(nbr_occurrences("Hello world !"))