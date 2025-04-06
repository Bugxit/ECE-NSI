def moyenne(tab):
    if not tab:
        return None
    
    somme = 0
    for x in tab:
        somme += x
    n = len(tab)
    return somme / n

print(moyenne([5,3,8]))
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
print(moyenne([]))
 # Comportement différent suivant le traitement proposé.
 # Ici None