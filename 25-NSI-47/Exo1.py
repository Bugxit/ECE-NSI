def taille(arbre, lettre):
    if lettre == '':
        return 0
    
    gauche = arbre[lettre][0]
    droit = arbre[lettre][1]
    
    taille_g = taille(a, gauche)
    taille_d = taille(a, droit)

    return taille_g + taille_d + 1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
 'H':['','']}

print(taille(a, 'F'))
print(taille(a, 'B'))
print(taille(a, 'I'))
