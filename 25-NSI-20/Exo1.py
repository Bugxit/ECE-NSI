def min_et_max(tab):
    dico = {"min" : tab[0], "max": tab[0]}
    for x in tab:
        if x < dico["min"]:
            dico["min"] = x
        if x > dico["max"]:
            dico["max"] = x
    return dico

print(min_et_max([0, 1, 4, 2,-2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3]))
print(min_et_max([-1,-1,-1,-1,-1]))