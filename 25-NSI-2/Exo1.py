def max_et_indice(tab):
    max_i = 0
    max_v = tab[0]
    for i, e in enumerate(tab):
        if e > max_v:
            max_i = i
            max_v = e
    
    return max_v, max_i

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1,-1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))