def couples_consecutifs(tab):
    n = len(tab)
    res = []
    for i in range(n - 1):
        if abs(tab[i] - tab[i + 1]) == 1:
            res.append((tab[i], tab[i+1]))
    
    return res

print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs([5, 1, 2, 3, 8,-5,-4, 7]))
