def ou_exclusif(tab1, tab2):
    res_tab = []
    for x, y in zip(tab1, tab2):
        res_tab.append(x ^ y)

    return res_tab

print(ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))
print(ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]))
