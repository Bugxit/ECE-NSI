def max_dico(dico):
    max_cle = 0
    max_valeur = float("-inf")
    for cle in dico:
        if dico[cle] > max_valeur:
            max_cle = cle
            max_valeur = dico[cle]
        
    return (max_cle, max_valeur)

print(max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 }))
print(max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 }))
