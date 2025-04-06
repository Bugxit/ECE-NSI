from random import randint

def lancer(n):
    tab = [randint(1, 6) for _ in range(n)]
    return tab

def paire_6(tab):
    nb_6 = 0
    for x in tab:
        if x == 6:
            nb_6 += 1
    
    return nb_6 >= 2

lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
lancer2 = lancer(5)
print(lancer2)
print(paire_6(lancer2))
lancer3 = lancer(3)
print(lancer3)
print(paire_6(lancer3))
lancer4 = lancer(0)
print(lancer4)
print(paire_6(lancer4))