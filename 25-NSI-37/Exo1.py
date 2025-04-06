def gb_vers_entier(tab):
    res = 0
    for bit in tab:
        res *= 2
        res += int(bit)

    return res

print(gb_vers_entier([]))
print(gb_vers_entier([True]))
print(gb_vers_entier([True, False, True,
 False, False, True, True]))
print(gb_vers_entier([True, False, False, False,
 False, False, True, False]))