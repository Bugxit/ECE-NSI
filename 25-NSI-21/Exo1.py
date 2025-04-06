def indices_maxi(tab):
    maxi = tab[0]
    indices = []
    for i, x in enumerate(tab):
        if x == maxi:
            indices.append(i)
        elif x > maxi:
            maxi = x
            indices = [i]

    return (maxi, indices)

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))