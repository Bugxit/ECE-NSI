def moyenne(tab):
    somme = 0
    coeff = len(tab)
    for x in tab:
        somme += x

    return somme / coeff

print(moyenne([1]))
print(moyenne([1, 2, 3, 4, 5, 6, 7]))
print(moyenne([1, 2]))