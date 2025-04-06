def occurrences(caractere, chaine):
    occ = 0
    for c in chaine:
        if c == caractere:
            occ += 1

    return occ

print(occurrences('e', "sciences"))
print(occurrences('i',"mississippi"))
print(occurrences('a',"mississippi"))