def fusion(tab1, tab2):
    new_tab = []
    i1 = i2 = 0
    n1 = len(tab1)
    n2 = len(tab2)
    while i1 < n1 and i2 < n2:
        if tab1[i1] < tab2[i2]:
            new_tab.append(tab1[i1])
            i1 += 1
        else:
            new_tab.append(tab2[i2])
            i2 += 1
    while i1 < n1:
        new_tab.append(tab1[i1])
        i1 += 1
    while i2 < n2:
        new_tab.append(tab2[i2])
        i2 += 1
    return new_tab

print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))
print(fusion([], []))
print(fusion([1, 2, 3], []))