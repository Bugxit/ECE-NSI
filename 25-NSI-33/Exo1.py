def insertion_abr(a, cle):
    g = a[0]
    v = a[1]
    d = a[2]
    if a[1] > cle:
        if a[0] is None:
            g = (None, cle, None)
        else:
            g = insertion_abr(a[0], cle)
    else:
        if a[2] is None:
            d = (None, cle, None)
        else:
            d = insertion_abr(a[2], cle)

    return (g, v, d)

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

print(insertion_abr(abr1, 4))
print(insertion_abr(abr1,-5))
print(insertion_abr(abr1, 2))
