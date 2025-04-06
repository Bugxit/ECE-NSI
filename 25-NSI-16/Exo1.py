def moyenne(notes):
    somme_notes = 0
    somme_coefs = 0
    for note, coef in notes:
        somme_notes += note * coef
        somme_coefs += coef

    moyenne = somme_notes / somme_coefs
    return moyenne

print(moyenne([(15.0,2),(9.0,1),(12.0,3)]))