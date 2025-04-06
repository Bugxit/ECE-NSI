def delta(liste):
    delta_liste = [liste[0]]
    for i in range(len(liste) - 1):
        x = liste[i+1] - liste[i]
        delta_liste.append(x)

    return delta_liste

print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))