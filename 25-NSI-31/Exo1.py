def recherche_motif(motif, texte):
    pos_liste = []
    for i in range(len(texte)):
        if texte[i:].startswith(motif):
            pos_liste.append(i)

    return pos_liste

print(recherche_motif("ab", ""))
print(recherche_motif("ab", "cdcdcdcd"))
print(recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))