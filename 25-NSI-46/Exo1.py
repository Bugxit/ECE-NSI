def compte_occurrences(x, tab):
    nbr = 0
    for e in tab:
        if x == e:
            nbr += 1
        
    return nbr

print(compte_occurrences(5, []))
print(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))
print(compte_occurrences('a', ['a','b','c','a','d','e','a']))