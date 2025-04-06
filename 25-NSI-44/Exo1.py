def moyenne(notes):
    somme_notes = 0
    somme_coefs = 0
    for note, coef in notes:
        somme_notes += note * coef
        somme_coefs += coef

    if somme_coefs == 0:
       return None

    return somme_notes / somme_coefs

print(moyenne([(8,2),(12,0),(13.5,1),(5,0.5)]))
print(moyenne([(3,0),(5,0)]))