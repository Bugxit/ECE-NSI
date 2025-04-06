def recherche(tab, n):
    i_elt = None
    for i, x in enumerate(tab):
        if x == n:
            i_elt = i
        
    return i_elt

print(recherche([5, 3],1))
print(recherche([2,4],2))
print(recherche([2,3,5,2,4],2))