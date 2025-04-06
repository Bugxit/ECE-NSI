def liste_puissances(a, n):
    liste = []
    x = a
    for _ in range(n):
        liste.append(x)
        x *= a

    return liste

def liste_puissances_borne(a, borne):
    liste = []
    x = a
    while x < borne:
        liste.append(x)
        x *= a 

    return liste

print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5)) 