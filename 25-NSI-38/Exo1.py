def moyenne(tab):
    somme = 0
    for x in tab:
        somme += x
    
    n = len(tab)
    return somme / n

print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))