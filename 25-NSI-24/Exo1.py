def enumere(tab):
    d = {c : [] for c in tab}
    for i, c in enumerate(tab):
        d[c].append(i)

    return d

print(enumere([]))
print(enumere([1, 2, 3]))
print(enumere([1, 1, 2, 3, 2, 1]))