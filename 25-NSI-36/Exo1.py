def nombre_de_mots(phrase):
    nbr_espace = 0
    for c in phrase:
        if c == ' ':
            nbr_espace += 1

    nbr_mot = nbr_espace + 1

    if phrase[-1] in ('?', '!'):
        nbr_mot -= 1

    return nbr_mot

print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est séparé !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))