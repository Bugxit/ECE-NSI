def ecriture_binaire_entier_positif(n):
    bin_str = ""
    while n:
        r = n % 2
        n = n // 2
        bin_str = str(r) + bin_str

    if not bin_str:
        bin_str = "0"

    return bin_str

print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))